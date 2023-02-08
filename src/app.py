from typing import Union, Dict

import kubernetes
import numpy as np
import pandas as pd

from src.evaluation.base import EvaluationFactory


class FeatureSelectionMaster:
    def __init__(self, environment, feature_type, image_name):
        self.environment = environment
        self.feature_type = feature_type
        self.image_name = image_name

        self.v1 = kubernetes.client.CoreV1Api()

    def train_and_evaluate(
            self,
            x: Union[pd.DataFrame, np.array],
            y: Union[pd.Series, np.array],
    ) -> float:
        evaluator = EvaluationFactory.generate_evaluator(self.environment, self.feature_type)
        return evaluator.train_and_evaluate(x, y)

    def score_features(
            self,
            x: Union[pd.DataFrame, np.array],
            y: Union[pd.Series, np.array],
            no_features_to_score: int = -1
    ) -> Dict:
        feature_scores = dict()
        no_columns = x.shape[1]
        if no_features_to_score == -1:
            no_features_to_score = no_columns

        for iteration in range(no_features_to_score):
            iteration_feature_scores = dict()
            for feature in range(no_columns):
                features_to_use = list(feature_scores) + [feature]
                prediction_score = self.train_and_evaluate(x[features_to_use], y)
                iteration_feature_scores[feature] = prediction_score
            iteration_winner = max(iteration_feature_scores, key=iteration_feature_scores.get)
            feature_scores[iteration_winner] = iteration + 1
        return feature_scores

    def get_pod_specification(self, task_id):
        return kubernetes.client.V1Pod(
            api_version="v1",
            kind="Pod",
            metadata=kubernetes.client.V1ObjectMeta(
                name=f"compute-pod-{task_id}"
            ),
            spec=kubernetes.client.V1PodSpec(
                containers=[
                    kubernetes.client.V1Container(
                        name=f"train-and-evaluate-{task_id}",
                        image=self.image_name,
                        command=["python", "-c",
                                 f"from from src.evaluation.base import EvaluationFactory;"
                                 f"evaluator = EvaluationFactory.generate_evaluator("
                                 f"{self.environment}, {self.feature_type});"
                                 f"evaluator.train_and_evaluate({x}, {y}));"  # x and y need should be passed to pod as JSON formatted environment variable
                                 f"evaluator.dump_results()"],
                    )
                ]
            )
        )

    def create_task(self, task_id):
        pod_spec = self.get_pod_specification(task_id)
        self.v1.create_namespaced_pod(body=pod_spec, namespace="default")

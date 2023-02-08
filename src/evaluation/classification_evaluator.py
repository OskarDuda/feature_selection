from enums.prediction_type import PredictionType
from evaluation.base import Evaluator, EvaluationFactory


@EvaluationFactory.register(PredictionType.CLASSIFICATION)
class ClassificationEvaluator(Evaluator):
    ...

from enums.model import PredictionType
from evaluation.base import Evaluator, EvaluationFactory


@EvaluationFactory.register(PredictionType.CLASSIFICATION)
class ClassificationEvaluator(Evaluator):
    ...

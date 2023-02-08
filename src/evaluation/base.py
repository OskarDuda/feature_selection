from abc import ABC
from typing import Union

import numpy as np
import pandas as pd


class Evaluator(ABC):
    def train_and_evaluate(self, x: Union[pd.DataFrame, np.array], y: Union[pd.Series, np.array]) -> float:
        raise NotImplemented


class EvaluationFactory:
    EVALUATORS = {}

    @classmethod
    def register(cls, prediction_type):
        ...

    @classmethod
    def generate_evaluator(cls, prediction_type) -> Evaluator:
        ...

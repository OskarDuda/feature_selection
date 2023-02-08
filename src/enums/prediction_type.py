from enum import Enum

from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeClassifier


class PredictionType(Enum):
    CLASSIFICATION = DecisionTreeClassifier
    REGRESSION = LinearRegression

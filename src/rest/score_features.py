from src.app import FeatureSelectionMaster


def score_features(no_features):
    fs = FeatureSelectionMaster()
    fs.score_features(no_features)

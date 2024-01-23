import joblib
import sklearn


def get_logregression_model():
    return joblib.load("ml/logreg_model.sav")


def gey_decision_tree_model():
    return joblib.load("ml/dectree_model.sav")

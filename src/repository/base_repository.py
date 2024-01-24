from src.ml import predictor_model
from src.model.predictor import Predictor

PREDICTOR_NAMES = ["LogReg", "TreeDecision"]


def get_predictor_by_name(name: str, session):
    predictor_db = session.query(Predictor).filter(Predictor.name == name).one()
    if predictor_db.name == "LogReg":
        return predictor_model.get_logregression_model()
    elif predictor_db.name in "TreeDecision":
        return predictor_model.gey_decision_tree_model()


def get_predictor_cost_by_name(name: str, session):
    predictor_db = session.query(Predictor).filter(Predictor.name == name).one()
    return predictor_db.cost

# def get_all_predictions_by_predictor_name(self, name: str):
#     predictor = self.session.query(Predictor).filter(Predictor.name == name).first()
#     return self.session.query(Prediction).filter(Prediction.predictor == predictor.name).all()

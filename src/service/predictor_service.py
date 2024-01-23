from src.repository import base_repository
from src.schema.base_schema import PredictionRequest


def make_prediction(schema: PredictionRequest, db):
    predictor = base_repository.get_predictor_by_name(schema.predictor_name, db)
    age = schema.age
    bilirubin = schema.bilirubin
    cholesterol = schema.cholesterol
    albumin = schema.albumin
    copper = schema.copper
    sgot = schema.sgot
    tryglicerides = schema.tryglicerides
    platelets = schema.platelets
    prothrombin = schema.prothrombin
    return predictor.predict([[age, bilirubin, cholesterol, albumin, copper,
                               sgot, tryglicerides, platelets, prothrombin]])

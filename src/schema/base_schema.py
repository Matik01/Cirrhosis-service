from pydantic import BaseModel


class Predictor(BaseModel):
    name: str
    cost: float
    is_active: bool

    class Config:
        orm_mode = True


# class Prediction(BaseModel):
#     predictor: Predictor().name
#     output_data: str
#
#     class Config:
#         orm_mode = True


class PredictionRequest(BaseModel):
    predictor_name: str
    age: float
    bilirubin: float
    cholesterol: float
    albumin: float
    copper: float
    sgot: float
    tryglicerides: float
    platelets: float
    prothrombin: float


class PredictionResponse(BaseModel):
    stage_result: int
from typing import Annotated
from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi import APIRouter, Depends, status
from src.model import user
from src.model import predictor
from src.core.database import engine
from src.schema.auth_schema import SignUp, SignUpResponse, SignInResponse
from src.schema.base_schema import PredictionRequest, PredictionResponse
from src.service import user_service
from src.service import predictor_service
from fastapi.templating import Jinja2Templates
from src.core.database import SessionLocal
from sqlalchemy.orm import Session
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

# prediction.Base.metadata.create_all(bind=engine)
predictor.Base.metadata.create_all(bind=engine)
user.Base.metadata.create_all(bind=engine)

bearer = HTTPBearer()

templates = Jinja2Templates(directory='src/templates')

router = APIRouter(
    prefix="/auth",
    tags=["auth"],
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/sign-in-action", response_model=SignInResponse)
async def sign_in_action(credentials: Annotated[HTTPAuthorizationCredentials, Depends(bearer)],
                         db: Session = Depends(get_db)):
    if credentials.scheme == "Bearer":
        logged_in_user = user_service.sign_in(db, token=credentials.credentials)
        return logged_in_user


@router.get('/sign-in', response_class=HTMLResponse)
def sign_in_page(request: Request):
    return templates.TemplateResponse('sign_in.html', {'request': request})


@router.post("/sign-up-action", response_model=SignUpResponse)
async def sign_up_action(user_info: SignUp, db: Session = Depends(get_db)):
    return user_service.sign_up(user_info, db)


@router.get('/sign-up', response_class=HTMLResponse)
def sign_in_page(request: Request):
    return templates.TemplateResponse('sign_up.html', {'request': request})


@router.post("/prediction-action", response_model=PredictionResponse)
async def prediction_action(credentials: Annotated[HTTPAuthorizationCredentials, Depends(bearer)],
                            prediction_request: PredictionRequest,
                            db: Session = Depends(get_db)):
    username = user_service.get_username_by_token(credentials.credentials, db)
    user_money = user_service.get_money_by_name(username, db)
    predictor_cost = predictor_service.get_predictor_cost(prediction_request, db)
    user_money_difference = user_money - predictor_cost
    print(user_money_difference)
    if user_money_difference < 0:
        return {"stage_result": "no money"}
    else:
        user_service.update_user_money(username, user_money_difference, db)
        predictor_result = {
            "stage_result": predictor_service.make_prediction(prediction_request, db)
        }
        return predictor_result


@router.get('/prediction', response_class=HTMLResponse)
def sign_in_page(request: Request):
    return templates.TemplateResponse('prediction.html', {'request': request})

from fastapi import APIRouter, Depends
from src.model import user
from src.model import predictor
from src.core.database import engine
from src.schema.auth_schema import SignIn, SignUp, SignUpResponse
from src.schema.base_schema import PredictionRequest, PredictionResponse
from src.service import user_service
from src.service import predictor_service
from fastapi.templating import Jinja2Templates
from src.core.database import SessionLocal
from sqlalchemy.orm import Session

# prediction.Base.metadata.create_all(bind=engine)
predictor.Base.metadata.create_all(bind=engine)
user.Base.metadata.create_all(bind=engine)

templates = Jinja2Templates(directory='templates')

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


@router.post("/sign-in-action")
async def sign_in_action(user_info: SignIn, db: Session = Depends(get_db)):
    return user_service.sign_in(db, token=user_info.token)


# @router.get('/sign-in', response_class=HTMLResponse)
# def sign_in_page(request: Request):
#     return templates.TemplateResponse('sign_in.html', {'request': request})


@router.post("/sign-up-action", response_model=SignUpResponse)
async def sign_up_action(user_info: SignUp, db: Session = Depends(get_db)):
    return user_service.sign_up(user_info, db)


# @router.get('/sign-up', response_class=HTMLResponse)
# def sign_in_page(request: Request):
#     return templates.TemplateResponse('sign_up.html', {'request': request})


@router.post("/prediction-action", response_model=PredictionResponse)
async def prediction_action(prediction_request: PredictionRequest, db: Session = Depends(get_db)):
    predictor_result = {
        "stage_result": predictor_service.make_prediction(prediction_request, db)
    }
    return predictor_result

# @router.get('/prediction', response_class=HTMLResponse)
# def sign_in_page(request: Request):
#     return templates.TemplateResponse('prediction.html', {'request': request})

from src.repository import user_repository
from src.schema import user_schema, auth_schema
from src.util import jwt_util
from fastapi import HTTPException, status
from fastapi.security import HTTPBearer
from fastapi import Depends

bearer = HTTPBearer()

credentials_exception = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Could not validate credentials",
    headers={"WWW-Authenticate": "Bearer"},
)


def get_user(schema: user_schema):
    return user_repository.get_user_by_name(schema.name)


def sign_up(schema: auth_schema, db):
    new_user = user_repository.create_user(schema, db)
    sign_up_result = {
        "name": new_user.name,
        "password": new_user.password,
        "token": new_user.token
    }
    return sign_up_result


def sign_in(db, token: str = Depends(bearer)):
    payload = jwt_util.decode_token(token)
    username = payload.get("name")
    if username is None:
        return credentials_exception
    user = user_repository.get_user_by_name(username, db)
    response_body = {
        "name": user.name,
        "money": user.money
    }
    return response_body


def get_token(schema: user_schema):
    user = user_repository.get_user_by_name(schema.name)
    return jwt_util.decode_token(user.token)


def get_user_money(schema: user_schema):
    user = user_repository.get_user_by_name(schema.name)
    return user.money

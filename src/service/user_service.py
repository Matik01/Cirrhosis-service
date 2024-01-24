from src.repository import user_repository
from src.schema import user_schema, auth_schema
from src.util import jwt_util
from fastapi import HTTPException, status

credentials_exception = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Could not validate credentials",
    headers={"WWW-Authenticate": "Bearer"},
)


def get_user(schema: user_schema):
    return user_repository.get_user_by_name(schema.name)


def sign_up(schema: auth_schema, db):
    new_user = user_repository.create_user(schema, db)
    print(new_user.token)
    sign_up_result = {
        "token": new_user.token
    }
    return sign_up_result


def sign_in(db, token: str):
    payload = jwt_util.decode_token(token)
    username = payload.get("sub")
    if username is None:
        return credentials_exception
    user = user_repository.get_user_by_name(username, db)
    user_repository.update_user_active_to_active(user.name, db)
    response_body = {
        "name": user.name,
        "money": user.money,
        "is_active": user.is_active
    }
    return response_body


def get_token(schema: user_schema, db):
    user = user_repository.get_user_by_name(schema.name, db)
    return jwt_util.decode_token(user.token)


def get_money_by_name(name: str, db):
    user = user_repository.get_user_by_name(name, db)
    return user.money


def get_username_by_token(token: str, db):
    return user_repository.get_username_by_token(token, db)


def update_user_money(name: str, money_difference: int, db):
    return update_user_money(name, money_difference, db)

from src.model.user import User
from src.schema import user_schema

from src.util import jwt_util


def get_user_by_index(self, index: int):
    return self.session.query(User).get(index)


def get_user_by_name(username: str, session):
    return session.query(User).filter(User.name == username).first()


def create_user(schema: user_schema, session):
    new_token = jwt_util.encode_token(schema.name, schema.password)
    new_user = User(name=schema.name, password=schema.password,
                    token=new_token)
    session.add(new_user)
    session.commit()
    return new_user


def update_user_token(schema: user_schema, token: str, session):
    user = get_user_by_name(schema)
    session.query(User).update(values={schema.name: token})
    session.commit()
    session.refresh(user)
    return user

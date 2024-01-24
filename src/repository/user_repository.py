from src.model.user import User
from src.schema import user_schema
from sqlalchemy import update
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


# def update_user_token(schema: user_schema, token: str, session):
#     user = get_user_by_name(schema.name, session)
#     session.query(user).update(values={schema.token: token})
#     session.commit()
#     session.refresh(user)
#     return

def get_username_by_token(token: str, session):
    user = session.query(User).filter(User.token == token).first()
    return user.name


def update_user_active_to_active(name: str, session):
    session.execute(update(User).where(User.name == name).values(is_active=True))
    session.commit()
    return


def update_user_money_by_name(name: str, money_difference: int, session):
    session.execute(update(User).where(User.name == name).values(money=money_difference))
    session.commit()
    return True

from pydantic import BaseModel


class SignInResponse(BaseModel):
    name: str
    money: int


class SignIn(BaseModel):
    name: str
    password: str
    token: str


class SignUp(BaseModel):
    name: str
    password: str


class SignUpResponse(BaseModel):
    name: str
    password: str
    token: str

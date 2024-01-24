from pydantic import BaseModel


class SignInResponse(BaseModel):
    name: str
    money: int
    is_active: bool


class SignIn(BaseModel):
    name: str
    password: str


class SignUp(BaseModel):
    name: str
    password: str


class SignUpResponse(BaseModel):
    token: str

from pydantic import BaseModel


class User(BaseModel):
    name: str
    password: str
    is_active: bool
    money: int
    token: str

    class Config:
        orm_mode = True

from pydantic import BaseModel


class RegisterUserSchema(BaseModel):
    name: str
    surname: str
    age: int


class UserSchema(BaseModel):
    id: int
    name: str
    surname: str
    age: int

    class Config:
        orm_mode = True

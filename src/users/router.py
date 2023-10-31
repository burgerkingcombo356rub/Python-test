from typing import List

from fastapi import APIRouter, Query

from .models import User
from .schemas import RegisterUserSchema, UserSchema
from .service import UserService

router = APIRouter(
    prefix='/users',
    tags=['Пользователи']
)


@router.get('/users-list/', summary='Список пользователей', description='Список пользователей')
async def users_list(
    min_age: int = Query(description='Минимальный возраст пользователей', default=0),
    max_age: int = Query(description='Максимальный возраст пользователей', default=200)
    ) -> List[UserSchema]:
    result = await UserService.find_beetween(User.age, min_age, max_age)
    return result


@router.post('/register-user/', summary='Регистрация пользователя', description='Регистрация пользователя')
async def register_user(
    name: str = Query(description="Имя пользователя"),
    surname: str = Query(description="Фамилия пользователя"),
    age: int = Query(description="Возраст пользователя")
    ) -> RegisterUserSchema:
    user = {'name': name, 'surname': surname, 'age': age}
    await UserService.add(**user)
    return user

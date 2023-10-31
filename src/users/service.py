from core.service import BaseService

from .models import User


class UserService(BaseService):
    model = User

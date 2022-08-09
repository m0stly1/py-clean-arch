from fastapi import APIRouter
from src.user import service


class UserApi():
    def __init__(self, service) -> None:
        self.user_service = service

    def register(self):
        user_api = APIRouter(prefix="/user")

        @user_api.get("")
        async def user():
            return await self.user_service.get_user()

        return user_api
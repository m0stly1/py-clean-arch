from src.models import user


class UserService:
    def __init__(self, repository) -> None:
        self.repository = repository

    async def get_user(self) -> user.User:
        return await self.repository.get_user()
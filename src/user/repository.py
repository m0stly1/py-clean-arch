from src.models import user
from src.core.database.mongo import Mongodb


class UserRepository:
    def __init__(self) -> None:
        self.db = Mongodb.create_connection()

    async def get_user(self, username) -> user.User:
        collection = self.db["users"]
        obj = collection.find_one({"username": username})
        print(obj)
        return user.User(
            username=obj["username"],
            email=obj["email"]
        )
        
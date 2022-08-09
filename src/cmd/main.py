from src.http.server import server
from src.http.api.user.user import UserApi
from src.user.service import UserService
from src.user.repository import UserRepository

from src.http.api.api import API

user_repository = UserRepository()
user_service = UserService(user_repository)
user_api = UserApi(user_service).register()

api = API().register(user_api)

app = server.create_http_server(api)
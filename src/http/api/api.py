from fastapi import APIRouter



class API:
    @classmethod
    def register(cls, user_api):
        api = APIRouter(prefix="/api")
        api.include_router(user_api)

        return api
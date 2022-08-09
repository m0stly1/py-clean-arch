import re
from fastapi import FastAPI
import datetime


def create_http_server(api):
    datetime_object = datetime.datetime.now()

    app = FastAPI()

    app.include_router(api)

    @app.on_event("startup")
    async def startup_event():
        with open("logs/server.txt", mode="a") as log:
            log.write(f'{datetime_object}\t Application startup \n')


    @app.on_event("shutdown")
    def shutdown_event():
        with open("logs/server.txt", mode="a") as log:
            log.write(f'{datetime_object}\t Application shutdown \n')
    
    return app





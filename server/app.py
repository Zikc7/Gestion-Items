

from fastapi import FastAPI

from .api import api_router
from .database import db_connection

gestion_items = FastAPI()

# ? Incluimos el router principal a la instancia de FastAPI
gestion_items.include_router(api_router)

@gestion_items.on_event("startup")
async def startup_event():
    """ if db_connection.connect():
        create_tables() """
    db_connection.connect()


@gestion_items.on_event("shutdown")
def shutdown_event():
    with open("log.txt", mode="a") as log:
        db_connection.disconnect
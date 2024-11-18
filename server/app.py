from fastapi import FastAPI

from .api import api_router

gestion_items = FastAPI()

#? Incluimos el router principal a la instancia de FastAPI
gestion_items.include_router(api_router)

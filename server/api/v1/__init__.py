from fastapi import APIRouter

from .project_routes import router as project_router

#! Router V1
router_v1 = APIRouter(prefix="/v1")

#? Agregar router v1 a rutas definidas
router_v1.include_router(project_router, tags=["Items"])
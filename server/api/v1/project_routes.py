from typing import Annotated, List

from fastapi import APIRouter, Path, Query

from server.schemas.items_schemas import NewItemRequest, ItemResponse, ItemRequest
from server.controller import ItemsController
from server.exceptions import InternalServerError,NotFound
router = APIRouter(prefix="/items")
router.responses = {
    500: InternalServerError.as_dict(),
}
controller = ItemsController()


@router.post(
    "",
    status_code=201,
    responses={
        201: {"description": "Item resgistrado"},
    },
    description="Crea un item con los campos creados en body param, falla si faltan campos obligatorios"
)  # ? POST /projects
async def Create(new_item: NewItemRequest) -> ItemResponse:
    # ? Recibir objeto
    return controller.create(new_item)


@router.get(
    "",
    status_code=200,
    responses={
        200: {"description": "Items Registrados"},
    },
    description="Retorna una lista paginada con los items registrados. Si no hay items retorna una lista vacia."
)  # ? GET /projects
async def get_list(limit: Annotated[int, Query(ge=1, le=1000)] = 10, offset: Annotated[int, Query(ge=0)] = 0) -> List[ItemResponse]:
    print(f"Paginado limite {limit} offset {offset}")
    return controller.get_list(limit,offset)


@router.get(
    "/{id}",
    status_code=200,
    responses={
        200: {"description": "Items Encontrado"},
        404: NotFound.as_dict(),
        422: {"description": "ID no es un entero valido"}
    },
    description="Retorna un item por id, falla si no existe el id."
)  # ? GET by ID/projects
async def get_by_id(id: Annotated[int, Path(ge=1)]) -> ItemResponse:
    return controller.get_by_id(id)


@router.patch(
    "/{id}",
    status_code=200,
    responses={
        200: {"description": "Items Actualizado"},
        404: NotFound.as_dict(),
        422: {"description": "ID no es un entero valido"}
    },
    description="Actualiza un Item con el body Para. Falla si el id no existe"
)  # ? PATCH/projects
async def update(id: Annotated[int, Path(ge=1)], item: ItemRequest) -> ItemResponse:
    return controller.update(id,item)


@router.delete(
    "/{id}",
    status_code=204,
    responses={
        204: {"description": "Items eliminado"},
        404: NotFound.as_dict(),
        422: {"description": "ID no es un entero valido"}
    },
    description="Elimina un item por id a travez del body param. Falla si el id no existe"
)  # ? DELETE/projects
async def delete(id: Annotated[int, Path(ge=1)]) -> None:
    controller.delete(id)

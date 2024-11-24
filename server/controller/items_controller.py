from typing import List

from fastapi import HTTPException

from server.schemas.items_schemas import NewItemRequest, ItemResponse, ItemRequest
from server.exceptions import BaseHTTPException, InternalServerError,NotFound


class ItemsController:
    def __init__(self):
        pass  # TODO: Referencia a servicio

    def create(self, new_item: NewItemRequest) -> ItemResponse:
        try:
            # TODO: llamar a capa servicio para que gestiones la acción correspondiente
            #! Retornar data de ejemplo
            return ItemResponse(id=1, **new_item.model_dump())
        except BaseHTTPException as ex:
            # TODO Implementar Logging
            raise ex
        except Exception:
            raise InternalServerError(
                "Error no contemplado, contacte al sysadmin")

    def get_list(self, limit: int, offset: int) -> List[ItemResponse]:
        try:
            # TODO: llamar a capa servicio para que gestiones la acción correspondiente
            #! Retornar data de ejemplo
            return []
        except BaseHTTPException as ex:
            # TODO Implementar Logging
            raise ex
        except Exception:
            raise InternalServerError(
                "Error no contemplado, contacte al sysadmin")

    def get_by_id(self, id: int) -> ItemResponse:
        try:
            # TODO: llamar a capa servicio para que gestiones la acción correspondiente
            #! Retornar data de ejemplo
            raise NotFound(f"Item con {id} no enconrado")
        except BaseHTTPException as ex:
            # TODO Implementar Logging
            raise ex
        except Exception:
            raise InternalServerError(
                "Error no contemplado, contacte al sysadmin")

    def update(self, id: int, new_data: ItemRequest) -> ItemResponse:
        try:
            # TODO: llamar a capa servicio para que gestiones la acción correspondiente
            #! Retornar data de ejemplo
            return ItemResponse(id=id, **new_data.model_dump(exclude_none=True))
        except BaseHTTPException as ex:
            # TODO Implementar Logging
            raise ex
        except Exception:
            raise InternalServerError(
                "Error no contemplado, contacte al sysadmin")

    def delete(self, id: int) -> None:
        try:
            # TODO: llamar a capa servicio para que gestiones la acción correspondiente
            return #
        except BaseHTTPException as ex:
            # TODO Implementar Logging
            raise ex
        except Exception:
            raise InternalServerError(
                "Error no contemplado, contacte al sysadmin")

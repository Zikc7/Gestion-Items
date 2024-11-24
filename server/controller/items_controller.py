from typing import List


from server.schemas.items_schemas import NewItemRequest, ItemResponse, ItemRequest
from server.exceptions import BaseHTTPException, InternalServerError
from server.service import ItemsService


class ItemsController:
    def __init__(self):
        self.service = ItemsService()

    def create(self, new_item: NewItemRequest) -> ItemResponse:
        try:
            return self.service.create(new_item)
        except BaseHTTPException as ex:
            # TODO Implementar Logging
            raise ex
        except Exception:
            raise InternalServerError(
                "Error no contemplado, contacte al sysadmin")

    def get_list(self, limit: int, offset: int) -> List[ItemResponse]:
        try:
            return self.service.get_list(limit,offset)
        except BaseHTTPException as ex:
            # TODO Implementar Logging
            raise ex
        except Exception:
            raise InternalServerError(
                "Error no contemplado, contacte al sysadmin")

    def get_by_id(self, id: int) -> ItemResponse:
        try:
            return self.service.get_by_id(id)
        except BaseHTTPException as ex:
            # TODO Implementar Logging
            raise ex
        except Exception:
            raise InternalServerError(
                "Error no contemplado, contacte al sysadmin")

    def update(self, id: int, new_data: ItemRequest) -> ItemResponse:
        try:
            return self.service.update(id,new_data)
        except BaseHTTPException as ex:
            # TODO Implementar Logging
            raise ex
        except Exception:
            raise InternalServerError(
                "Error no contemplado, contacte al sysadmin")

    def delete(self, id: int) -> None:
        try:
            self.service.delete(id)
        except BaseHTTPException as ex:
            # TODO Implementar Logging
            raise ex
        except Exception:
            raise InternalServerError(
                "Error no contemplado, contacte al sysadmin")

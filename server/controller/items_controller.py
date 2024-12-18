import logging
from typing import List


from server.schemas.items_schemas import NewItemRequest, ItemResponse, ItemRequest
from server.exceptions import BaseHTTPException, InternalServerError
from server.service import ItemsService

logger = logging.getLogger(__name__)


class ItemsController:
    def __init__(self):
        self.service = ItemsService()

    def create(self, new_item: NewItemRequest) -> ItemResponse:
        try:
            logger.debug(f"Create Item{new_item.name}")
            return self.service.create(new_item)
        except BaseHTTPException as ex:
            self.__handler_http_exception(ex)
        except Exception:
            logger.critical(f"Error no contemplado en {__name__}.create()")
            raise InternalServerError(
                "Error no contemplado, contacte al sysadmin")

    def get_list(self, limit: int, offset: int) -> List[ItemResponse]:
        try:
            return self.service.get_list(limit, offset)
        except BaseHTTPException as ex:
            self.__handler_http_exception(ex)
        except Exception:
            logger.critical(f"Error no contemplado en {__name__}.get_list()")
            raise InternalServerError(
                "Error no contemplado, contacte al sysadmin")

    def get_by_id(self, id: int) -> ItemResponse:
        try:
            logger.debug(f"Buscar item #{id}")
            return self.service.get_by_id(id)
        except BaseHTTPException as ex:
            self.__handler_http_exception(ex)
        except Exception as ex:
            logger.critical(f"Error no contemplado en {__name__}.get_by_id()")
            raise InternalServerError()

    def update(self, id: int, new_data: ItemRequest) -> ItemResponse:
        try:
            return self.service.update(id,new_data)
        except BaseHTTPException as ex:
            self.__handler_http_exception(ex)
        except Exception as ex2:
            logger.critical(f"Error no contemplado en {__name__}.update()")
            raise InternalServerError(ex2)

    def delete(self, id: int) -> None:
        try:
            return self.service.delete(id)
        except BaseHTTPException as ex:
            self.__handler_http_exception(ex)
        except Exception as ex2:
            logger.critical(f"Error no contemplado en {__name__}.delete()")
            raise InternalServerError(f"Error no contemplado, contacte al sysadmin {ex2}")

    def __handler_http_exception(self, ex: BaseHTTPException):
        if ex.status_code >= 500:
            logger.critical(f"Error en el servidor con status code: {
                            ex.status_code}: {ex.description}")
        else:
            logger.error(f"Error: {
                ex.status_code}: {ex.description}")
        raise ex

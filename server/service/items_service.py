from typing import List
from server.schemas.items_schemas import NewItemRequest, ItemResponse, ItemRequest
from server.exceptions import NotFound


class ItemsService:
    last_id: int = 0
    fake_db: list[dict] = []

    def __init__(self):
        # TODO instanciar repo
        pass

    def create(self, new_item: NewItemRequest) -> ItemResponse:
        # TODO:
        #! 1. Recibir el objeto de tipo NewItemResponse, convertilo a dic5t y pasarlo a la capa service
        #! 2. recibir del repo la respuesta (probalbemente un dict u objeto) y convertilo a ItemResponse y retornarlo
        # ? Ejemplo
        item_dict = self.__fake_create(new_item.model_dump())
        return ItemResponse(**item_dict)

    def get_list(self, limit: int, offset: int) -> List[ItemResponse]:
        # TODO:
        #! 1. Recibir los parametros limit y offset y pasarlos a la capa repo
        #! 2. Recibir la lista de dict u objetos y convertirlos a una lista de ItemResponse y retornar
        # ? Ejemplo
        item_list = self.__fake_get_list(limit, offset)
        return [ItemResponse(**item) for item in item_list]

    def get_by_id(self, id: int) -> ItemResponse:
        # TODO:
        #! 1. Recibir el id de los paramatetros y pasarlo a la capa repo
        #! 2. Recibimos el objeto o diccionario del repo y lo convertimos a un ItemResponse, para retornarlo
        item = self.__fake_get_by_id(id)
        if item is None:
            raise NotFound(f"Item con id #{id} no encontrado")
        return ItemResponse(**item)

    def update(self, id: int, new_data: ItemRequest) -> ItemResponse:
        # TODO:
        #! 1. Recibimos los parametros, convertimos el new_data a dict y lo pasamos al repo
        #! 2. Reccibimos el objeto actualizado del repo y lo convertimos en ItemResponse para retornarlo
        update_item = self.__fake_update(
            id, new_data.model_dump(exclude_none=True))
        if update_item is None:
            raise NotFound(f"Item con id #{id} no encontrado para actualizar")
        return ItemResponse(**update_item)

    def delete(self, id: int) -> None:
        # TODO:
        #! 1. Pasamos el Id al repo y retornamos
        if not self.__fake_delete(id):
            raise NotFound(f"Item no encontrado #{id} para eliminarse")
        # ? FAKE METHODS

    def __fake_create(self, new_item: dict) -> dict:
        from datetime import datetime
        now = datetime.now()
        ItemsService.last_id += 1
        new_item.update(
            id=ItemsService.last_id,
            created_at=now,
            updated_at=now,
        )
        ItemsService.fake_db.append(new_item)
        return new_item

    def __fake_get_list(self, limit: int, offset: int) -> list[dict] | None:
        db_size = len(ItemsService.fake_db)
        firts_index = min(db_size, offset)
        last_index = max((db_size - firts_index), limit)
        return ItemsService.fake_db[firts_index:last_index]

    def __fake_get_by_id(self, id: int) -> dict | None:
        for item in ItemsService.fake_db:
            if item["id"] == id:
                return item

    def __fake_update(self, id: int, new_data: dict) -> dict:
        from datetime import datetime
        now = datetime.now()
        current_item = self.__fake_get_by_id(id)
        if current_item is None:
            return
        current_item.update(**new_data, updated_at=now)
        return current_item

    def __fake_delete(self, id: int) -> bool:
        current_item = self.__fake_get_by_id(id)
        if current_item is None:
            return False
        ItemsService.fake_db.remove(current_item)
        return True

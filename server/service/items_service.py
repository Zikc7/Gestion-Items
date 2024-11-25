from typing import List
from server.schemas.items_schemas import NewItemRequest, ItemResponse, ItemRequest
from server.exceptions import NotFound
from server.repository import ItemsRepository


class ItemsService:

    def __init__(self):
        self.item_repo = ItemsRepository()

    def create(self, new_item: NewItemRequest) -> ItemResponse:
        item_dict = self.item_repo.create(new_item.model_dump())
        return ItemResponse(**item_dict)

    def get_list(self, limit: int, offset: int) -> List[ItemResponse]:
        item_list = self.item_repo.get_list(limit, offset)
        return [ItemResponse(**item) for item in item_list]

    def get_by_id(self, id: int) -> ItemResponse:
        item = self.item_repo.get_by_id(id)
        if item is None:
            raise NotFound(f"Item con id #{id} no encontrado")
        return ItemResponse(**item)

    def update(self, id: int, new_data: ItemRequest) -> ItemResponse:
        updated_item = self.item_repo.update(
            id, new_data.model_dump(exclude_none=True))
        if updated_item is None:
            raise NotFound(f"Item con id #{id} no encontrado para actualizar")
        return ItemResponse(**updated_item)
    def delete(self, id: int) -> None:
        if not self.item_repo.delete(id):
            raise NotFound(f"Item no encontrado #{id} para eliminarse")

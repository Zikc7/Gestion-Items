from server.database import db_connection
from server.database.models import ItemModel


class ItemsRepository:

    def __init__(self):
        self.db = db_connection.session

    def create(self, new_item_dict: dict) -> dict:
        new_item = ItemModel(**new_item_dict)
        self.db.add(new_item)
        self.db.commit()
        self.db.refresh(new_item)
        return self.__to_dict(new_item)

    def get_list(self, limit: int, offset: int) -> list[dict] | None:
        items = self.db.query(ItemModel).order_by(
            "id").limit(limit).offset(offset).all()
        return [self.__to_dict(item) for item in items]

    def get_by_id(self, item_id: int) -> dict | None:
        item = self.__get_one(item_id)
        if item is None:
            return
        return self.__to_dict(item)

    def update(self, id: int, new_data: dict) -> dict | None:
        item = self.__get_one(id)
        if item is None: return
        for field in new_data.keys():
            setattr(item, field, new_data[field])
        self.db.commit()
        self.db.refresh(item)
        return self.__to_dict(item)

    def delete(self, id: int) -> bool:
        item = self.__get_one(id)
        if item is None:
            return False 
        self.db.delete(item)
        self.db.commit()
        return True

    def __get_one(self, item_id: int) -> ItemModel | None:
        return self.db.query(ItemModel).filter_by(id=item_id).first()

    def __to_dict(self, item: ItemModel) -> dict:
        return {
            column.name: getattr(item, column.name)
            for column in ItemModel.__table__.columns
        }

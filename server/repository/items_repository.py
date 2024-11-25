from server.database import db_connection
from server.database.models import ItemModel


class ItemsRepository:

    def __init__(self):
        self.db = db_connection.session

    def create(self, new_item_dict: dict) -> dict:
        """ from datetime import datetime
        now = datetime.now()
        ItemsRepository.last_id += 1
        new_item.update(
            id=ItemsRepository.last_id,
            created_at=now,
            updated_at=now,
        )
        ItemsRepository.fake_db.append(new_item)
        return new_item """
        new_item = ItemModel(**new_item_dict)
        self.db.add(new_item)
        self.db.commit()
        self.db.refresh(new_item)
        return self.__to_dict(new_item)

    def get_list(self, limit: int, offset: int) -> list[dict] | None:
        """ db_size = len(ItemsRepository.fake_db)
        firts_index = min(db_size, offset)
        last_index = min(db_size, (firts_index + limit))
        return ItemsRepository.fake_db[firts_index:last_index] """
        items = self.db.query(ItemModel).order_by(
            "id").limit(limit).offset(offset).all()
        return [self.__to_dict(item) for item in items]

    def get_by_id(self, item_id: int) -> dict | None:
        """ for item in ItemsRepository.fake_db:
            if item["id"] == id:
                return item """
        item = self.__get_one(item_id)
        if item is None:
            return
        return self.__to_dict(item)

    def update(self, id: int, new_data: dict) -> dict | None:
        """ from datetime import datetime
        now = datetime.now()
        current_item = self.get_by_id(id)
        if current_item is None: return
        current_item.update(**new_data, updated_at=now)
        return current_item """
        item = self.__get_one(id)
        if item is None: return
        for field in new_data.keys():
            setattr(item, field, new_data[field])
        self.db.commit()
        self.db.refresh(item)
        return self.__to_dict(item)

    def delete(self, id: int) -> bool:
        """ current_item = self.get_by_id(id)
        if current_item is None:
            return False
        ItemsRepository.fake_db.remove(current_item)
        return True """
        item = self.__get_one()
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

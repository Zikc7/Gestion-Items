from datetime import datetime

from pydantic import BaseModel


class NewItemRequest(BaseModel):
    name: str
    proveedor: str = "New"
    marca: str = ""


class ItemRequest(BaseModel):
    name: str | None = None
    proveedor: str | None = None
    marca: str | None = None


class ItemResponse(BaseModel):
    id: int
    name: str
    proveedor: str = "New"
    marca: str = ""
    create_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()

from datetime import datetime

from pydantic import BaseModel


class NewItemRequest(BaseModel):
    title: str
    status: str = "New"
    description: str = ""


class ItemRequest(BaseModel):
    title: str | None = None
    status: str | None = None
    description: str | None = None


class ItemResponse(BaseModel):
    id: int
    title: str
    status: str = "New"
    description: str = ""
    create_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()

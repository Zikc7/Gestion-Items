from datetime import datetime

from pydantic import BaseModel



class NewItemRequest(BaseModel):
    title:str
    status: str = "New"
    description: str = ""

class ItemResponse(BaseModel):
    id: int
    title:str
    status: str = "New"
    description: str = "prueba"
    create_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()

class ItemRequest(BaseModel):
    title:str | None = None
    status: str | None = None
    description: str | None = None

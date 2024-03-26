from typing import Optional
from pydantic import BaseModel, HttpUrl

class ItemSchema(BaseModel):
    id: Optional[int] = None
    nome: str
    chamado_id: Optional[int]
    class Config:
        orm_mode = True
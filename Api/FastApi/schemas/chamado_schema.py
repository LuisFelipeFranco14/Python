from typing import Optional
from typing import List
from pydantic import BaseModel
from schemas.item_schema import ItemSchema

class ChamadoSchema(BaseModel):
    id: Optional[int] = None
    titulo: str
    descricao: str
    status_chamado: chr
    usuario_id: Optional[int]

    class Config:
        orm_mode = True

class ChamadoSchemaItens(ChamadoSchema):
    itens: Optional[List[ItemSchema]]
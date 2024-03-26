from typing import Optional
from typing import List
from pydantic import BaseModel, EmailStr
from schemas.chamado_schema import ChamadoSchema

class UsuarioSchemaBase(BaseModel):
    id: Optional[int] = None
    login: str
    email: EmailStr
    ed_admin: bool = False

    class Config:
        orm_mode = True

class UsuarioSchemaCreate(UsuarioSchemaBase):
    senha: str

class UsuarioSchemaChamados(UsuarioSchemaBase):
    chamados: Optional[List[ChamadoSchema]]

class UsuarioSchemaUp(UsuarioSchemaBase):
    login: Optional[str]
    email: Optional[str]
    senha: Optional[str]
    eh_admin: Optional[bool]
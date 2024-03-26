from fastapi import APIRouter

from api.v1.endpoints import chamado
from api.v1.endpoints import item
from api.v1.endpoints import usuario


api_router = APIRouter()

api_router.include_router(item.router, prefix='/itens', tags=['itens'])
api_router.include_router(chamado.router, prefix='/chamados', tags=['chamados'])
api_router.include_router(usuario.router, prefix='/usuarios', tags=['usuarios'])
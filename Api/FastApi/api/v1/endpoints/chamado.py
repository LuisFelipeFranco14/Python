from typing import List
from fastapi import APIRouter, status, Depends, HTTPException, Response

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from models.chamado_model import ChamadoModel
from models.usuario_model import UsuarioModel
from schemas.chamado_schema import ChamadoSchema, ChamadoSchemaItens
from core.deps import get_session, get_current_user

router = APIRouter()

# Post Chamado
@router.post('/', status_code=status.HTTP_201_CREATED, response_model=ChamadoSchema)
async def post_chamado(chamado: ChamadoSchema, Usuario_logado: UsuarioModel = Depends(get_current_user), db: AsyncSession = Depends(get_session)):
    novo_chamado: ChamadoModel = ChamadoModel(titulo=chamado.titulo, descricao=chamado.descricao,status_chamado=chamado.status_chamado, usuario_id=Usuario_logado.id)

    db.add(novo_chamado)
    await db.commit()

    return novo_chamado

#Get chamados
@router.get('/', response_model=List[ChamadoSchema])
async def get_chamados(db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(ChamadoModel)
        result = await session.execute(query)
        chamados: List[ChamadoModel] = result.scalars().unique().all()

        return chamados
     
#Get Chamado
@router.get('/{chamado_id}', response_model=ChamadoSchemaItens, status_code=status.HTTP_200_OK)
async def get_chamado(chamado_id: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(ChamadoModel).filter(ChamadoModel.id == chamado_id)
        result = await session.execute(query)
        chamado: ChamadoSchemaItens = result.scalars().unique().one_or_none()

        if chamado:
             return chamado
        else:
             raise HTTPException(detail='Chamado não encontrado', status_code=status.HTTP_404_NOT_FOUND) 
        
#Put Chamado
@router.put('/{chamado_id}', response_model=ChamadoSchema, status_code=status.HTTP_202_ACCEPTED)
async def get_chamado(chamado_id: int, chamado: ChamadoSchema, db: AsyncSession = Depends(get_session), usuario_logado: UsuarioModel =  Depends(get_current_user)):
    async with db as session:
        query = select(ChamadoModel).filter(ChamadoModel.id == chamado_id)
        result = await session.execute(query)
        chamado_up: ChamadoModel = result.scalars().unique().one_or_none()

        if chamado_up:
             
             if chamado.titulo:
                chamado_up.titulo = chamado.titulo 
             if chamado.descricao:
                chamado_up.descricao = chamado.descricao
             if chamado.status_chamado:
                chamado_up.status_chamado = chamado.status_chamado
             if usuario_logado.id != chamado_up.usuario_id:
                chamado_up.usuario_id = usuario_logado.id 

             await session.commit()

             return chamado_up
        else:
             raise HTTPException(detail='Chamado não encontrado', status_code=status.HTTP_404_NOT_FOUND) 
        
#Delete Chamado
@router.delete('/{chamado_id}', status_code=status.HTTP_204_NO_CONTENT)
async def get_chamado(chamado_id: int, db: AsyncSession = Depends(get_session), usuario_logado: UsuarioModel =  Depends(get_current_user)):
    async with db as session:
        query = select(ChamadoModel).filter(ChamadoModel.id == chamado_id).filter(ChamadoModel.usuario_id == usuario_logado.id)
        result = await session.execute(query)
        chamado_del: ChamadoModel = result.scalars().unique().one_or_none()

        if chamado_del:
            await session.delete(chamado_del)
            await session.commit()
            return Response(status_code=status.HTTP_204_NO_CONTENT)
        else:
             raise HTTPException(detail='Chamado não encontrado', status_code=status.HTTP_404_NOT_FOUND) 
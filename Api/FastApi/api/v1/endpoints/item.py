from typing import List

from fastapi import APIRouter, status, Depends, HTTPException, Response

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from models.item_model import ItemModel
from models.usuario_model import UsuarioModel
from schemas.item_schema import ItemSchema
from core.deps import get_session, get_current_user


router = APIRouter()


# POST Item
@router.post('/{chamado_id}', status_code=status.HTTP_201_CREATED, response_model=ItemSchema)
async def post_item(chamado_id: int, item: ItemSchema,db: AsyncSession = Depends(get_session)):
    novo_item: ItemSchema = ItemSchema(nome=item.nome, chamado_id=item.chamado_id)

    db.add(novo_item)
    await db.commit()

    return novo_item


# GET Itens
@router.get('/{chamado_id}', response_model=List[ItemSchema])
async def get_itens(chamado_id: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(ItemModel).filter(ItemModel.chamado_id == chamado_id)
        result = await session.execute(query)
        itens: List[ItemModel] = result.scalars().unique().all()

        return itens


# GET Item
@router.get('/{item_id}&{chamado_id}', response_model=ItemSchema, status_code=status.HTTP_200_OK)
async def get_item(item_id, chamado_id: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(ItemModel).filter(ItemModel.id == item_id).filter(ItemModel.chamado_id == chamado_id)
        result = await session.execute(query)
        item: ItemModel = result.scalars().unique().one_or_none()

        if item:
            return item
        else:
            raise HTTPException(detail='Item não encontrado',
                                status_code=status.HTTP_404_NOT_FOUND)


# PUT Item
@router.put('/{item_id}&{chamado_id}', response_model=ItemSchema, status_code=status.HTTP_202_ACCEPTED)
async def put_item(item_id, chamado_id: int, item: ItemSchema, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(ItemModel).filter(ItemModel.id == item_id).filter(ItemModel.chamado_id == chamado_id)
        result = await session.execute(query)
        item_up: ItemModel = result.scalars().unique().one_or_none()

        if item_up:
            if item.nome:
                item_up.nome = item.nome
            if item.chamado_id:
                item_up.chamado_id = item.chamado_id    

            await session.commit()

            return item_up
        else:
            raise HTTPException(detail='Item não encontrado',
                                status_code=status.HTTP_404_NOT_FOUND)


# DELETE Item
@router.delete('/{item_id}&{chamado_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_item(item_id, chamado_id: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(ItemModel).filter(ItemModel.id == item_id).filter(ItemModel.chamado_id == chamado_id)
        result = await session.execute(query)
        item_del: ItemModel = result.scalars().unique().one_or_none()

        if item_del:
            await session.delete(item_del)
            await session.commit()

            return Response(status_code=status.HTTP_204_NO_CONTENT)
        else:
            raise HTTPException(detail='Item não encontrado',
                                status_code=status.HTTP_404_NOT_FOUND)

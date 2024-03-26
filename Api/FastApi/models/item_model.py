from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from core.configs import settings

class ItemModel(settings.DBBaseModel):
    __tablename__ = 'itens'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(256))
    chamado_id = Column(Integer, ForeignKey('chamados.id'))
    chamado = relationship("ChamadoModel", back_populates='itens', lazy='joined')
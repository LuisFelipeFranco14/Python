from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from core.configs import settings

class ChamadoModel(settings.DBBaseModel):
    __tablename__ = 'chamados'

    id = Column(Integer, primary_key=True, autoincrement=True)
    titulo = Column(String(256))
    descricao = Column(String(256))
    status_chamado = Column(chr(1))
    usuario_id = Column(Integer, ForeignKey('usuarios.id'))
    criador = relationship("UsuarioModel", back_populates='chamados', lazy='joined')
    itens = relationship(
        "ItemModel",
        cascade="all, delete-orphan",
        back_populates="chamado",
        uselist=True,
        lazy="joined"
    )
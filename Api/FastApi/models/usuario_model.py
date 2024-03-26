from sqlalchemy import Integer, String, Column, Boolean
from sqlalchemy.orm import relationship

from core.configs import settings

class UsuarioModel(settings.DBBaseModel):
    __table__ = 'usuarios'

    id = Column(Integer, primary_key=True, autoincrement=True)
    login = Column(String(256), index=True, nullable=False, unique=True)
    email = Column(String(256), index=True, nullable=False, unique=True)
    senha = Column(String(256), nullable=False)
    eh_admin = Column(Boolean, default=False)
    artigos = relationship(
        "ChamadoModel",
        cascade="all, delete-orphan",
        back_populates="criador",
        uselist=True,
        lazy="joined"
    )

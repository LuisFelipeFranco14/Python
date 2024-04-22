from typing import List, ClassVar

from pydantic_settings import BaseSettings
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.decl_api import DeclarativeMeta

class Settings(BaseSettings):
    API_ROUTER_PRIMARY: str = '/api/Principal'
    DB_URL: str = 'postgresql+asyncpg://adaptus:Solution@localhost:5432/EsteiraPedidos' 
    DBBaseModel: ClassVar[str] =  declarative_base()

    JWT_SECRET: str = '17cE8zLBlfTmDqUHcTfD6WICKDpFLaGfFS51uzwvGOA'
    """
    Como gerar Secrets no terminal 
    import secrets
    token: str = secrets.token_urlsafe(32)
    """
    ALGORITHM:  str = 'HS256'

    # 60 minutos * 24 horas * 7 dias => 1 semana 
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7

    class Config:
        case_sensitive = True

settings: Settings = Settings() 

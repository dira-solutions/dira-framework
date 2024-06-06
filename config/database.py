from pydantic import Field, BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Any

from diracore.support.config import DatabaseConfig as BaseDatabaseConfig
from diracore.support.config.database import (
    ConnectionDBConfig as BaseConnectionDBConfig, 
    ModelsDBConfig as BaseModelsDBConfig
)

class ConnectionDBConfig(BaseSettings):
    model_config = SettingsConfigDict(
        env_file='.env', 
        env_file_encoding='utf-8', 
        validate_default=False,
        extra='allow'
    )
    url: str = Field(alias='db_url', default=None)
    host: str = Field(alias='db_host', default='127.0.0.1')
    port: str = Field(alias='db_port', default='5432')
    database: str = Field(alias='db_database', default='forge')
    username: str = Field(alias='db_username', default='forge')
    password: str = Field(alias='db_password', default='')
    charset: str = Field(alias='utf8', default=None)
    prefix: str = Field(alias='', default=None)
    prefix_indexes: str = Field(default=True)
    search_path: str = Field(default='public')
    sslmode: str = Field(default='prefer')
    
class ConnectionSqliteConfig(ConnectionDBConfig):
    url: str = Field(alias='db_url', default='database/db.sqlite')

class ModelsDBConfig(BaseModelsDBConfig):
    path: list[str] = ["app/entity/"]

class DatabaseConfig(BaseDatabaseConfig):
    default: str = Field(alias='db_connection', default=None)
    connections: dict[str, Any] = {
        "sqlite": ConnectionSqliteConfig().model_dump(),
        "pgsql": ConnectionDBConfig().model_dump(),
    }
    models: ModelsDBConfig = ModelsDBConfig()
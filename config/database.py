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
    prefix_indexes: str|bool = Field(default=True)
    search_path: str = Field(default='public')
    sslmode: str = Field(default='prefer')

class ConnectionSqliteConfig(ConnectionDBConfig):
    url: str = Field(alias='db_url', default='database/sql/db.sqlite')
    file_path: str = Field(alias='db_path', default='database/sql/db.sqlite')
    

class ConnectionRedisConfig(BaseSettings):
    url: str|None = Field(alias='redis_url', default=None)
    host: str = Field(alias='redis_host', default='127.0.0.1')
    port: str = Field(alias='redis_port', default='6379')
    db: str|int = Field(alias='redis_database', default=0)
    username: str = Field(alias='redis_username', default='')
    password: str = Field(alias='redis_password', default='')


class ModelsDBConfig(BaseModelsDBConfig):
    path: list[str] = ["app/entity/"]


class DatabaseConfig(BaseDatabaseConfig):
    default: str = Field(alias='db_connection', default=None)
    connections: dict[str, Any] = {
        "sqlite": ConnectionSqliteConfig().model_dump(),
        "pgsql": ConnectionDBConfig().model_dump(),
    }
    models: ModelsDBConfig = ModelsDBConfig()
    migration_path: str = Field(alias='db_migration_path', default='./database/migrations')

    redis: dict[str, Any] = {
        "default": ConnectionRedisConfig().model_dump()
    }
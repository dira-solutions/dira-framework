from pydantic import Field

from diracore.support.config import DatabaseConfig as BaseDatabaseConfig
from diracore.support.config.database import (
    ConnectionDBConfig as BaseConnectionDBConfig, 
    ModelsDBConfig as BaseModelsDBConfig
)

class ConnectionDBConfig(BaseConnectionDBConfig):
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


class ModelsDBConfig(BaseModelsDBConfig):
    path: list[str] = ["app/entity/"]


class DatabaseConfig(BaseDatabaseConfig):
    default: str = Field(alias='db_connection', default=None)
    connections: dict[str, ConnectionDBConfig] = Field(default={
        "pgsql": ConnectionDBConfig()
    })
    models: ModelsDBConfig = ModelsDBConfig()
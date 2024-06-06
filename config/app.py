from app.providers import (
    app_service,
    route_service,
    route_service,
    auth_service,
)

from diracore.support.service_provider import ServiceProvider
from diracore.support.auth.middleware import JWTAuthentication
from diracore.foundation.support.providers.middleware_service import MiddlewareServiceProvider

from diracore.support.config import AppConfig as BaseAppConfig

import os
from urllib.parse import urlparse
from typing import List, Dict, Any, Tuple
from pydantic import Field
from pydantic_settings import BaseSettings


def default_url():
    if ":" in os.getenv("APP_URL", []):
        parsed_url = urlparse(os.getenv("APP_URL"))
        __host = parsed_url.geturl()
        __port = parsed_url.port or 8000
    else:
        __host = os.getenv("APP_URL", 'localhost')
        __port = os.getenv("APP_PORT", "8000")
        
    return [__host, __port]


class AppConfig(BaseSettings):
    env: str = Field(alias='app_env', default='local')
    url: str = Field(alias='app_url', default='localhost')
    host: str = Field(alias='app_host', default=default_url()[0])
    port: str|int = Field(alias='app_port', default=default_url()[1])
    
    providers: Any = ServiceProvider.default_list() + [
        MiddlewareServiceProvider,
        app_service.AppServiceProvider,
        route_service.RouteServiceProvider,
        auth_service.AuthServiceProvider,
    ]
    middlewares: Dict[str, Any] = {
        'api:auth': JWTAuthentication
    }
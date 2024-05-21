from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

from diracore.foundation.http.http_kernel import HttpKernel

from contextlib import asynccontextmanager
from pydantic_settings import BaseSettings

from config import Config

import os


class Kernel(HttpKernel):
    @asynccontextmanager
    async def lifespan(self, app: FastAPI):
        await self.bootstrap()
        yield

    def sync_middleware_to_router(self):
        return

    def handle(self):
        self._app.bind(BaseSettings, Config)
        
        dependencies = [
            # ....
        ]
        title = os.getenv("APP_NAME", "DIRA Framework")
        self.server = FastAPI(
            lifespan=self.lifespan, 
            title=title, 
            dependencies=dependencies,
            default_response_class=ORJSONResponse
        )
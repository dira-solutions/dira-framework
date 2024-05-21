from diracore.support.service_provider import ServiceProvider
from diracore.contracts.routing.http_router import HttpRouter
from fastapi import APIRouter

class AppServiceProvider(ServiceProvider):
    def register(self):
        self.app.bind(HttpRouter, APIRouter)
        pass

    def boot(self):
        pass
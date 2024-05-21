from app.http.controllers.controller import Controller

from diracore.routing.router import Route
from diracore.main import app

route: Route = app.make(Route)

route.get('/123', Controller.index).middleware()
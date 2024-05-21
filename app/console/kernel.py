from diracore.foundation.console.console_kernel import ConsoleKernel
from pydantic_settings import BaseSettings

from config import Config

class Kernel(ConsoleKernel):
    def handle(self):
        self._app.bind(BaseSettings, Config)
        return super().handle()

    def commands(self) -> None:
        self.load('app.console.commands.*')
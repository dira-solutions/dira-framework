
from diracore.contracts.foundation.application import Application as ApplicationContract
from diracore.contracts.kernel import Kernel as KernelContract
from diracore.main import app

from app.console.kernel import ConsoleKernel
from app.http.kernel import HttpKernel

def cli():
    app.singleton(ApplicationContract, lambda: app)
    app.singleton(KernelContract, ConsoleKernel)
    kernel = app.make(KernelContract)
    kernel.handle()

def serve():

    app.singleton(ApplicationContract, lambda: app)
    app.singleton(KernelContract, HttpKernel)
    kernel = app.make(KernelContract)
    kernel.handle()

    return kernel.send()
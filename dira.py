
from diracore.contracts.foundation.application import Application as ApplicationContract
from diracore.contracts.kernel import Kernel as KernelContract
from diracore.main import app

def cli():
    from app.console.kernel import Kernel

    app.singleton(ApplicationContract, lambda: app)
    app.singleton(KernelContract, Kernel)
    kernel: Kernel = app.make(KernelContract)
    kernel.handle()


def serve():
    from app.http.kernel import Kernel

    app.singleton(ApplicationContract, lambda: app)
    app.singleton(KernelContract, Kernel)
    kernel = app.make(KernelContract)
    kernel.handle()

    return kernel.send()
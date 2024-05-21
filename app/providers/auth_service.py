from diracore.support.auth.model import User
from diracore.support.auth.service import AuthServiceProvider as AuthBaseServiceProvider

class AuthServiceProvider(AuthBaseServiceProvider):
    async def register(self):
        await super().register()
    
    def jwt_middleware(self, user_model=User):
        return super().jwt_middleware(user_model)

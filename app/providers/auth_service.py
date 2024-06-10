from app.entity.user import User
from diracore.support.http.auth.service import AuthServiceProvider as AuthBaseServiceProvider

class AuthServiceProvider(AuthBaseServiceProvider):
    async def register(self):
        await super().register()
    
    def jwt_middleware(self, user_model=User):
        return super().jwt_middleware(user_model)

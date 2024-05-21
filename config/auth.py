from pydantic import Field

from diracore.support.config import AuthConfig as BaseAuthConfig

class AuthConfig(BaseAuthConfig):
    secret_key: str = Field(alias='auth_secret_key', default='your-secret-key')
    algorithm: str = Field(alias='auth_algorithm', default='HS256')
    token_expire_minutes: int = Field(alias='auth_token_expire_minutes', default=2*60)
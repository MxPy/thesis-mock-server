from functools import lru_cache

from pydantic import BaseSettings, root_validator


class Settings(BaseSettings):
    MINIO_ROOT_USER: str = "username"
    MINIO_ROOT_PASSWORD: str = "password"
    MINIO_HOST: str = "minio"
    MINIO_PORT: int = 9000
    MINIO_SECURE: bool = False
    MINIO_BUCKET_NAME: str = "minio-bucket"
    MINIO_URI: str = None

    @root_validator
    def uri_validator(cls, values) -> dict:
        values["MINIO_URI"] = f'{values["MINIO_HOST"]}:{values["MINIO_PORT"]}'
        return values


@lru_cache()
def get_settings():
    return Settings()


settings = get_settings()
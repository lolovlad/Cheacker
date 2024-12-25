from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    redis_password: str
    redis_user: str
    redis_user_password: str

    redis_host: str
    redis_port: int

    minio_access_key: str
    minio_secret_key: str
    minio_default_buckets: str
    minio_host: str
    minio_port: int


settings = Settings(_env_file=".env", _env_file_encoding="utf-8")

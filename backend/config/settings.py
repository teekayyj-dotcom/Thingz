from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field, SecretStr
from typing import Optional

# Sử dụng Pydantic để quản lý cấu hình từ biến môi trường
class Settings(BaseSettings):
    """
    Quản lý các biến môi trường. Pydantic sẽ tự động đọc từ tệp .env (nếu có)
    và từ các biến môi trường của hệ thống/Docker.
    """
    model_config = SettingsConfigDict(
        env_file=".env", 
        extra="ignore"
    )

    # Cấu hình Database
    DB_USER: str = Field("postgres", description="Tên người dùng PostgreSQL")
    DB_PASSWORD: str = Field("password", description="Mật khẩu PostgreSQL")
    DB_HOST: str = Field("localhost", description="Host của PostgreSQL")
    DB_PORT: int = Field(5432, description="Cổng của PostgreSQL")
    DB_NAME: str = Field("ecommerce_db", description="Tên Database")

    # URL kết nối Database sử dụng asyncpg driver cho SQLAlchemy
    @property
    def DATABASE_URL(self) -> str:
        """Tạo URL kết nối CSDL theo định dạng asyncpg"""
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    # Cấu hình JWT (Bảo mật)
    SECRET_KEY: SecretStr = Field(..., description="Khóa bí mật dùng để ký JWT")
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    REFRESH_TOKEN_EXPIRE_DAYS: int = 7
    
    # Cấu hình Celery & Redis
    REDIS_HOST: str = Field("localhost", description="Host của Redis")
    REDIS_PORT: int = Field(6379, description="Cổng của Redis")
    CELERY_BROKER_URL: Optional[str] = None # Sẽ được tính toán sau

# Khởi tạo instance Settings để sử dụng trong toàn bộ dự án
settings = Settings()

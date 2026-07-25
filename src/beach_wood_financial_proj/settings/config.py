from pathlib import Path
from typing import Annotated, Optional
from pydantic import Field, BeforeValidator
from pydantic_settings import BaseSettings, SettingsConfigDict

# Base Directory of the Django application (src/)
BASE_DIR = Path(__file__).resolve().parent.parent.parent


# 1. Environment file path configuration
def get_env_file_path() -> Path:
    """Always return the single standard .env file path."""
    return BASE_DIR / ".env" / ".env"


# 2. Helper to parse comma-separated strings (like ALLOWED_HOSTS) into lists
def parse_comma_separated(v: any) -> list[str]:
    if isinstance(v, str):
        # Handle string wrapped in parentheses or quotes
        cleaned = v.strip("()[]\"' ")
        return [
            item.strip().strip("'\"") for item in cleaned.split(",") if item.strip()
        ]
    return v


CommaSeparatedList = Annotated[str | list[str], BeforeValidator(parse_comma_separated)]


# 3. Settings Schema Definition
class AppSettings(BaseSettings):
    STAGE_ENVIRONMENT: str
    ALLOWED_HOSTS: CommaSeparatedList
    INTERNAL_IPS: CommaSeparatedList = Field(default=[])
    DEBUG: bool = False
    SECRET_KEY: str
    ENCRYPT_KEY: str
    BACKUP_KEY: str
    COMPRESS_LEVEL: int = 5
    MANAGER_MAIN_EMAIL: str = "manager@beachwoodfinancial.com"
    SITE_DOMAIN: str = "127.0.0.1:8000"
    SITE_NAME: str = "Ledger Flare"
    LANGUAGE_CODE: str = "en-us"
    TIME_ZONE: str = "UTC"
    USE_I18N: bool = True
    USE_TZ: bool = True

    # DB settings
    DB_ENGINE: str = "django.db.backends.postgresql"
    DB_HOST: str = "127.0.0.1"
    DB_NAME: str
    DB_USER: str
    DB_PASSWORD: str
    DB_PORT: int = 5432
    DB_CLIENT_ENCODING: str = "UTF8"

    # Cache settings
    CACHE_BACKEND_ENGINE: str = "django_valkey.cache.ValkeyCache"
    IS_CACHE_ENABLED: bool = False
    VALKEY_HOST: str = "127.0.0.1"
    VALKEY_PASSWORD: str = ""
    VALKEY_PORT: int = 6379

    # Redis/Alternative Cache settings
    REDIS_HOST: str = "127.0.0.1"
    REDIS_USER: str = "default"
    REDIS_PASSWORD: str = ""
    REDIS_PORT: int = 6379

    # Sessions/Security settings
    SESSION_COOKIE_AGE: int = 3600
    SESSION_EXPIRE_SECONDS: int = 3600
    SESSION_EXPIRE_AT_BROWSER_CLOSE: bool = True
    SESSION_EXPIRE_AFTER_LAST_ACTIVITY: bool = True

    # Sentry settings
    SENTRY_SDK_DSN: str = ""
    SENTRY_IS_ENABLED: bool = False

    # Optional settings that might not be in all envs
    STATICFILES_STORAGE: str = "whitenoise.storage.CompressedStaticFilesStorage"
    ENABLE_SELECTIVE_SECURITY_LOGGING: bool = False
    SECURITY_LOG_SAMPLING_RATE: float = 1.0
    EXPORTED_FROM_CLI_DIR: str = ""
    OLD_PRODUCTION_SECRET_KEY: str = ""
    INIT_DB_COMMAND_FILE_NAME: str = ""
    WHEREAMI: str = "LOCAL"

    # CORS & CSRF
    CORS_ALLOWED_ORIGINS: CommaSeparatedList = Field(default=[])
    CSRF_TRUSTED_ORIGINS: CommaSeparatedList = Field(default=[])

    model_config = SettingsConfigDict(
        env_file_encoding="utf-8",
        extra="ignore",  # Ignore extra values in the env file
    )


# 4. Global verified settings instance
app_settings = AppSettings(_env_file=get_env_file_path())

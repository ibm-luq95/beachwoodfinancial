from pathlib import Path

from decouple import Config, RepositoryEnv

cwd = Path.cwd()
# env_path = cwd / ".env" / ".env"
env_path = cwd / ".env" / ".env_docker"  # For docker

# check if .env file not exists
if env_path.exists() is False:
    raise Exception(".env file not exists!!!")

config = Config(RepositoryEnv(env_path))

environment = config("STAGE_ENVIRONMENT", cast=str)

# logger.info(f" Environment is: ({environment})")

if environment == "DEV":
    from .dev import *
elif environment == "PRODUCTION":
    from .production import *
elif environment == "TEST":
    from .test import *
elif environment == "LOCAL":
    from .local import *
elif environment == "STAGE":
    from .stage import *
elif environment == "LOCAL_DEV":
    from .local_dev import *

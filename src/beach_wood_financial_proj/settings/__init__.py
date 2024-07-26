from pathlib import Path

from decouple import Config, RepositoryEnv
import configparser

cwd = Path.cwd()
config = configparser.RawConfigParser()
stage_env_file = cwd / ".env" / "current_stage.ini"
if stage_env_file.exists() is False:
    raise Exception("stage file not exists!!!".upper())
config.read(stage_env_file)
stage = config.get("environment", "STAGE_ENVIRONMENT")
# print(stage)
if stage == "DOCKER":
    env_path = cwd / ".env" / ".env_docker"  # For docker
elif stage == "LOCAL_DEV":
    env_path = cwd / ".env" / ".env"  # For local


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

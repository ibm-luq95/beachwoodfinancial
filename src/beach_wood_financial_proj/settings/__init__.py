import os

from decouple import Config, RepositoryEnv

cwd = os.getcwd()
full_env_file_path = os.path.join(cwd, ".env", ".env_dev")

config = Config(RepositoryEnv(full_env_file_path))

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

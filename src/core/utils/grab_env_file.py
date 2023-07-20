# -*- coding: utf-8 -*-#

from django.conf import settings
from decouple import Config, RepositoryEnv


def grab_env_file(env_file_name: str = ".env") -> Config:
    """
    This function will use only in django project, views, models,..etc
    Don't ues it outside the django project
    Parameters
    ----------
    env_file_name: str = this will be the .env file name, in case using files other than .env file (default)

    Returns
    -------
        Config: Config = config object of .env variables
    """
    env_file_path = settings.BASE_DIR / ".env" / env_file_name
    if env_file_path.exists() is False:
        raise Exception(".env file not exists!!!")
    config = Config(RepositoryEnv(env_file_path))
    return config

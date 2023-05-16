# -*- coding: utf-8 -*-#

from django.conf import settings
from decouple import Config, RepositoryEnv


def grab_env_file(env_file_name: str = ".env_dev") -> Config:
    env_file_path = settings.BASE_DIR / ".env" / env_file_name
    config = Config(RepositoryEnv(env_file_path))
    return config

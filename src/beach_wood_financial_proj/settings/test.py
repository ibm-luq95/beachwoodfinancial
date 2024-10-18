import logging
# from .base import *
from .dev import *

logging.disable()

ALLOWED_HOSTS = ["127.0.0.1"]

# DEBUG = True

DEBUG_TOOLBAR_CONFIG = {
    "SHOW_TOOLBAR_CALLBACK": show_toolbar,
    "IS_RUNNING_TESTS": True,
    "RENDER_PANELS": None,
}

# DATABASES["TEST"] = {
#     "ENGINE": "django.db.backends.mysql",
#     "NAME": "DB_NAME",
#     "USER": "DB_USER",
#     "PASSWORD": "DB_PASSWORD",
#     "HOST": "localhost",  # Or an IP Address that your DB is hosted on
#     "PORT": "3306",
# }

STORAGES = {
    "default": {"BACKEND": "django.core.files.storage.InMemoryStorage"},
    "staticfiles": {"BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage"},
}

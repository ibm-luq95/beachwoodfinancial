import logging
# from .base import *
from .dev import *

logging.disable()

ALLOWED_HOSTS = ["127.0.0.1"]

# Remove Debug Toolbar from tests to prevent NoReverseMatch and SystemCheckErrors
if "debug_toolbar" in INSTALLED_APPS:
    INSTALLED_APPS.remove("debug_toolbar")
MIDDLEWARE = [m for m in MIDDLEWARE if "debug_toolbar" not in m]

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

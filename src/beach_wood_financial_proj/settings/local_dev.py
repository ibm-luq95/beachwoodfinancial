# -*- coding: utf-8 -*-#
from .dev import *

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "local_dev.sqlite3",
    }
}

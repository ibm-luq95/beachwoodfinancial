from .dev import *

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
        "TEST": {
            "NAME": BASE_DIR / "mytestdatabase.sqlite3",
            "ENGINE": "django.db.backends.sqlite3",
        },
    },

}

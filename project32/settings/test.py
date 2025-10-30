from .dev import *

DEBUG = False
SECRET_KEY = "insecure-test-key"

PASSWORD_HASHERS = [
    "django.contrib.auth.hashers.MD5PasswordHasher",
]

EMAIL_BACKEND = "django.core.mail.backends.locmem.EmailBackend"

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
        "LOCATION": "project32-test-cache",
    }
}

DATABASES["default"]["TEST"] = {
    "NAME": DATABASES["default"].get("NAME", "project32") + "_test",
}

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {"console": {"class": "logging.StreamHandler"}},
    "root": {"handlers": ["console"], "level": "WARNING"},
}

import tempfile, os
_TMP_DIR = tempfile.gettempdir()
MEDIA_ROOT = os.path.join(_TMP_DIR, "project32_media_test")
STATIC_ROOT = os.path.join(_TMP_DIR, "project32_static_test")

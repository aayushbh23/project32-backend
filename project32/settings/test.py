# project32/settings/test.py
from .dev import *  # or ".base" if you split settings; dev is fine as a base for test

# Keep tests predictable & fast
DEBUG = False
SECRET_KEY = "insecure-test-key"  # fine for tests

# Fast password hashing speeds up test suite a lot
PASSWORD_HASHERS = [
    "django.contrib.auth.hashers.MD5PasswordHasher",
]

# In-memory email box for assertions
EMAIL_BACKEND = "django.core.mail.backends.locmem.EmailBackend"

# Local-memory cache so tests don't require Redis/Memcached
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
        "LOCATION": "project32-test-cache",
    }
}

# Test database (separate from dev DB). If you use Postgres in dev, keep the same ENGINE
# and just point TEST NAME to a throwaway DB name. Pytest will create/drop it.
# If your dev settings already read env vars for DB, this override is usually enough.
DATABASES["default"]["TEST"] = {
    "NAME": DATABASES["default"].get("NAME", "project32") + "_test",
}

# Optional: cut noisy logging during tests
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {"console": {"class": "logging.StreamHandler"}},
    "root": {"handlers": ["console"], "level": "WARNING"},
}

# Media/Static to tmp dirs so file uploads in tests don’t touch real folders
import tempfile, os
_TMP_DIR = tempfile.gettempdir()
MEDIA_ROOT = os.path.join(_TMP_DIR, "project32_media_test")
STATIC_ROOT = os.path.join(_TMP_DIR, "project32_static_test")

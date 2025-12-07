# covidapp/settings/test.py
from .base import *

DEBUG = False
ALLOWED_HOSTS = ["*"]

# Use in-memory SQLite for faster tests
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
    }
}
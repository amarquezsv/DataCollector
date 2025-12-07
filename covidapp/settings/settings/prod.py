# covidapp/settings/prod.py
from .base import *

DEBUG = False
ALLOWED_HOSTS = ["yourdomain.com"]

# Example: switch to PostgreSQL in production
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "covidapp",
        "USER": "youruser",
        "PASSWORD": "yourpassword",
        "HOST": "localhost",
        "PORT": "5432",
    }
}
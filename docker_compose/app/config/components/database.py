import os

DATABASES = {
    "default": {
        "ENGINE": os.environ.get(
            "POSTGRES_DB_ENGINE",
            default="django.db.backends.postgresql"
        ),
        "NAME": os.environ.get("POSTGRES_DB", default='movies_database'),
        "USER": os.environ.get("POSTGRES_USER", default=None),
        "PASSWORD": os.environ.get("POSTGRES_PASSWORD", default=None),
        "HOST": os.environ.get("POSTGRES_DB_HOST", default='127.0.0.1'),
        "PORT": os.environ.get("POSTGRES_DB_PORT", default=5432),
        "OPTIONS": {"options": "-c search_path=public,content"},
    }
}

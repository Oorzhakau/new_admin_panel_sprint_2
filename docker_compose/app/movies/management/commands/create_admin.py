import os

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

User = get_user_model()


class Command(BaseCommand):
    def handle(self, *args, **options):
        username = os.environ.get("DJ_SU_ADMIN", "admin")
        email = os.environ.get("DJ_SU_EMAIL", "admin@mail.com")
        password = os.environ.get("DJ_SU_PASSWORD", "!QAZ1qaz")
        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(
                username=username,
                email=email,
                password=password,
            )

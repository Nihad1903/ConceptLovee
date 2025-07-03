from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
import os
from decouple import config

class Command(BaseCommand):
    help = 'Create a superuser if not exists, using env vars'

    def handle(self, *args, **kwargs):
        User = get_user_model()

        username = config('DJANGO_SUPERUSER_USERNAME')
        email = config('DJANGO_SUPERUSER_EMAIL')
        password = config('DJANGO_SUPERUSER_PASSWORD')
        print(username)
        print(email)
        print(password)
        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(username=username, email=email, password=password)
            self.stdout.write(self.style.SUCCESS(f'Superuser "{username}" created successfully.'))
        else:
            self.stdout.write(f'Superuser "{username}" already exists.')
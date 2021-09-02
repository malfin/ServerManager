from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

from authapp.models import UserProfile


class Command(BaseCommand):
    help = 'Create default users'

    def handle(self, *args, **options):
        UserProfile.objects.create_superuser(username='kpk', password='pass')
        UserProfile.objects.create_user(username='user1', password='pass')
        print('user created')

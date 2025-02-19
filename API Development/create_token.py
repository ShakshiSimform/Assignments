import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'task_manager.settings')
django.setup()

from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

user = User.objects.get(username='shakshi')
token, created = Token.objects.get_or_create(user=user)
print(token.key)

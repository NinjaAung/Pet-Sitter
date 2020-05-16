from django.test import TestCase
from django.contrib.auth.models import User
from django.utils import timezone
import datetime

from pets.models import Pet, Appointment


class UserTest(TestCase):
    def user_login(self):
        user = User.objects.create_user(
            username='testing', 
            password='testing'
            )

        self.client.login(
            username='testing', 
            password='testing')
        

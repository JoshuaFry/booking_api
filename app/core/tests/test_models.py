from django.test import TestCase

from django.contrib.auth import get_user_model
from core.models import User, Session


class UserModelTests(TestCase):

    def test_create_user(self):
        """Test user creation"""
        user = get_user_model().objects.create(
            email='test@test.test',
            first_name='Test',
            username='Test',
            password='pass123456!'
        )

        users = User.objects.filter(username='Test')

        self.assertEqual(len(users), 1)

    def test_create_user_fails_with_no_username(self):
        """Test user creation fails with no username"""
        user = get_user_model().objects.create(
            email='test@test.test',
            first_name='Test',
            password='pass123456!'
        )

        users = User.objects.filter(username='Test')

        self.assertEqual(len(users), 0)


class SessionModelTests(TestCase):

    def test_create_session(self):
        """Test session creation"""



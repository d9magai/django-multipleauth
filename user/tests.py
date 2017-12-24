from django.conf import settings
from django.contrib.auth import login
from django.contrib.auth.models import User as AuthUser
from django.test import TestCase
from django.urls import reverse
from pprint import pprint

from app.models import User, Owner


class UserTest(TestCase):

    def setUp(self):
        settings.SESSION_COOKIE_NAME = 'user_sessionid'

    def test_user_login(self):
        """Redirect to 302, when not logined user is accessed."""
        response = self.client.get(reverse('user:index'))
        self.assertEqual(response.status_code, 302)
        """User login, access to index page test"""
        email = 'hoge@fuga.com'
        password = 'password'
        user = User.objects.create_user(email)
        user.set_password(password)
        user.save()
        self.assertTrue(self.client.login(username=email, password=password))
        response = self.client.get(reverse('user:index'))
        """success"""
        self.assertEqual(response.status_code, 200)

    def test_owner_login(self):
        """Redirect to 302, when not logined user is accessed."""
        response = self.client.get(reverse('user:index'))
        self.assertEqual(response.status_code, 302)
        """Owner login, access to index page test"""
        email = 'hoge@fuga.com'
        password = 'password'
        owner = Owner.objects.create_user(email)
        owner.set_password(password)
        owner.save()
        self.assertTrue(self.client.login(username=email, password=password))
        response = self.client.get(reverse('user:index'))
        """redirect to login page"""
        self.assertEqual(response.status_code, 302)

    def test_auth_user_login_failed(self):
        """Redirect to 302, when not logined user is accessed."""
        response = self.client.get(reverse('user:index'))
        self.assertEqual(response.status_code, 302)
        """AuthUser login, access to index page test"""
        username = 'foo'
        password = 'bar'
        user = AuthUser.objects.create_user(username, password=password)
        user.is_superuser = False
        user.is_staff = False
        user.save()
        self.assertTrue(self.client.login(username=username, password=password))
        response = self.client.get(reverse('user:index'))
        """redirect to login page"""
        self.assertEqual(response.status_code, 302)

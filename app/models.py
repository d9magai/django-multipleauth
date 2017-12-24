from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractBaseUser, UserManager
from django.db import models


class OwnerManager(UserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('missing email')
        user = self.model(email=email)
        user.set_password(make_password(password))
        user.save(using=self._db)
        return user


class Owner(AbstractBaseUser):
    name = models.CharField(max_length=128)
    email = models.EmailField(
        max_length=254,
        unique=True,
        db_index=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    objects = OwnerManager()
    USERNAME_FIELD = 'email'

    def is_staff(self):
        return False

    def has_perm(self, perm, obj=None):
        return False

    def has_module_perms(self, app_label):
        return False


class UserManager(UserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('missing email')
        user = self.model(email=email)
        user.set_password(make_password(password))
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    name = models.CharField(max_length=128)
    email = models.EmailField(
        max_length=254,
        unique=True,
        db_index=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    objects = UserManager()
    USERNAME_FIELD = 'email'

    def is_staff(self):
        return False

    def has_perm(self, perm, obj=None):
        return False

    def has_module_perms(self, app_label):
        return False

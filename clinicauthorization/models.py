from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
class UserManager(BaseUserManager):
    def create_user(self, email, name, password=None, is_admin=False):
        if not email:
            raise ValueError("Users must have an email address")
        user = self.model(email=self.normalize_email(email), name=name, is_admin=is_admin)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password=None):
        return self.create_user(email, name, password=password, is_admin=True)

class User(AbstractBaseUser):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.email

    
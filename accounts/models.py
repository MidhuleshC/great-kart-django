import email
from django.db import models
from django.contrib.auth.models import AbstractBaseUser ,BaseUserManager
from django.forms import CharField

# Create your models here.

class MyAccountManager(BaseUserManager):
    def create_user(self,first_name,last_name,user_name,email,password = None):
        if not email:
            raise ValueError('Email required.')

        if not user_name:
            raise ValueError('user name required.')

        user = self.model(
            email = self.normalize_email(email),
            user_name = user_name,
            first_name= first_name,
            last_name = last_name
         )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,first_name,last_name,user_name,email,password):
        user = self.create_user(
            email = self.normalize_email(email),
            user_name = user_name,
            first_name= first_name,
            last_name = last_name,
            password = password
        )
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    user_name = models.CharField(max_length=100 ,unique=True)
    email = models.EmailField(max_length=190 ,unique=True)
    phone_number = models.CharField(max_length=20)

    # required
    date_joined = models. DateTimeField(auto_now_add=True)
    last_login = models. DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name','first_name','last_name']

    objects = MyAccountManager()

    def __str__(self) -> str:
        return super().__str__()
        # return self.email

    def has_perm(self,perm,obj = None):
        return self.is_admin

    def has_module_perms(self,add_label):
        return True

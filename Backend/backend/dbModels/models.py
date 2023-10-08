from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager, User
from django.core.cache import cache
import datetime

class CustomAccountManager(BaseUserManager):

    def create_superuser(self, username, password, **other_fields):
        other_fields.setdefault("is_superuser", True)
        other_fields.setdefault("is_staff", True)

        if other_fields.get("is_superuser") is not True and other_fields.get("is_stuff") is not True:
            raise ValueError("bad setter of privilegie")
        return self.create_user(username, password, **other_fields)

    def create_user(self, username, password, **other_fields):
        user_now = self.model(username=username, **other_fields)
        user_now.set_password(password)
        user_now.save()
        return user_now


class DjangoUser(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(primary_key=True, auto_created=True)
    email = models.EmailField(blank=True, null=True, unique=True)
    username = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(blank=True, null=True, max_length=150)
    last_name = models.CharField(blank=True, null=True, max_length=150)
    is_staff = models.BooleanField(default=False)

    #education_group = models.ForeignKey("models.EducationGroup", on_delete=models.CASCADE, blank=True, null=True)
    #user_type = models.ForeignKey("UserType", on_delete=models.CASCADE, blank=True, null=True)
    #grade = models.ForeignKey("models.Class", on_delete=models.CASCADE, blank=True, null=True)
    #shortcut = models.CharField(max_length=5,blank=True,null=True)

    objects = CustomAccountManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []

    def save(self, *args, **kwargs):
        super(User, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        super(User, self).delete(*args, **kwargs)

    def __str__(self):
        return self.username

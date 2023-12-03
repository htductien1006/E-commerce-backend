from django.db import models
from django.contrib.auth import models as auth_model
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

# Create your models here.


class ShoppingSession(models.Model):
    total = models.IntegerField(null=False, default=0)
    user_id = models.ForeignKey(
        "user_service.User", on_delete=models.CASCADE, to_field="id", default=0)


class CustomAccountManager(auth_model.BaseUserManager):

    def create_superuser(self, email, username, first_name, password, **other_fields):

        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')

        return self.create_user(email, username, first_name, password, **other_fields)

    def create_user(self, email, username, first_name, password, **other_fields):

        if not email:
            raise ValueError(_('You must provide an email address'))

        email = self.normalize_email(email)
        user = self.model(email=email, username=username,
                          first_name=first_name, **other_fields)
        user.set_password(password)
        user.save()
        return user


class User(auth_model.AbstractUser, auth_model.PermissionsMixin):
    # --Required--
    first_name = models.CharField(verbose_name="First Name", max_length=255)
    last_name = models.CharField(verbose_name="Last Name", max_length=255)
    username = models.CharField(verbose_name="User Name", max_length=255)
    email = models.EmailField(verbose_name="Email",
                              max_length=255, unique=True)
    # --Unnessary--
    phone_number = models.CharField(verbose_name="Phone Number")
    country = models.CharField(verbose_name="Country")
    address = models.CharField(verbose_name="Address")
    postal_code = models.CharField(verbose_name="Postal Code")

    objects = CustomAccountManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name", "username"]

    def __str___(self):
        return self.username

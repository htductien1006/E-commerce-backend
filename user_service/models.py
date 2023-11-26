from django.db import models
from django.contrib.auth import models as auth_model

# Create your models here.


class Admin(auth_model.BaseUserManager):

    def create_user(
        self,
        first_name: str,
        last_name: str,
        username: str,
        email: str,
        password: str = None,
        is_staff=False,
        is_superuser=False,
    ) -> "User":
        if not email:
            raise ValueError("User must have an email")
        if not first_name:
            raise ValueError("User must have a first name")
        if not last_name:
            raise ValueError("User must have a last name")
        if not username:
            raise ValueError("User must have username")

        user = self.model(email=self.normalize_email(email))
        user.first_name = first_name
        user.last_name = last_name
        user.username = username
        user.set_password(password)
        user.is_active = True
        user.is_staff = is_staff
        user.is_superuser = is_superuser
        user.save()

        return user

    def create_superuser(
        self, first_name: str, last_name: str, email: str, username: str, password: str
    ) -> "User":
        user = self.create_user(
            first_name=first_name,
            last_name=last_name,
            email=email,
            username=username,
            password=password,
            is_staff=True,
            is_superuser=True,
        )
        user.save()

        return user


class User(auth_model.AbstractUser):
    # --Required--
    first_name = models.CharField(verbose_name="First Name", max_length=255)
    last_name = models.CharField(verbose_name="Last Name", max_length=255)
    username = models.CharField(verbose_name="User Name", max_length=255)
    email = models.EmailField(verbose_name="Email",
                              max_length=255, unique=True)
    password = models.CharField(max_length=255)
    # --Unnessary--
    phone_number = models.CharField(verbose_name="Phone Number")
    country = models.CharField(verbose_name="Country")
    address = models.CharField(verbose_name="Address")
    postal_code = models.CharField(verbose_name="Postal Code")

    objects = Admin()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name", "username"]

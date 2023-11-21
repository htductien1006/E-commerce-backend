from django.db import models
from django.contrib.auth import models as auth_model

# Create your models here.
class User(auth_model.AbstractUser):
    #--Required--
    first_name = models.CharField(verbose_name="First Name", max_length=255)
    last_name = models.CharField(verbose_name="Last Name", max_length=255)
    username = models.CharField(verbose_name="User Name", max_length=255)
    password = models.CharField(verbose_name="Password")
    phone_number = models.CharField(verbose_name="Phone Number", unique=True)
    #--Unnessary--
    email = models.CharField(verbose_name="Email", unique=True)
    country = models.CharField(verbose_name="Country")
    address = models.CharField(verbose_name="Address")
    postal_code = models.CharField(verbose_name="Postal Code")

    USERNAME_FIELD="username"
    REQUIRED_FIELDS=["first_name","last_name","password"]


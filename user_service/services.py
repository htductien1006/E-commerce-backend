import dataclasses
import datetime
import jwt
from rest_framework import exceptions
from typing import TYPE_CHECKING
from django.conf import settings
from django.shortcuts import get_object_or_404
from . import models

if TYPE_CHECKING:
    from .models import User


@dataclasses.dataclass
class UserDataClass:
    first_name: str
    last_name: str
    email: str
    username: str
    password: str = None
    id: int = None

    @classmethod
    def from_instance(cls, user: "User") -> "UserDataClass":
        return cls(
            id=user.id,
            first_name=user.first_name,
            last_name=user.last_name,
            email=user.email,
            username=user.username
        )


def create_user(user_dc: "UserDataClass") -> "UserDataClass":
    instance = models.User(
        first_name=user_dc.first_name, last_name=user_dc.last_name, email=user_dc.email, username=user_dc.username
    )
    if user_dc.password is not None:
        instance.set_password(user_dc.password)

    instance.save()

    return UserDataClass.from_instance(instance)


def user_email_selector(email: str) -> "User":
    user = models.User.objects.filter(email=email).first()

    return user


def create_token(user_id: int) -> str:
    payload = dict(
        id=user_id,
        exp=datetime.datetime.utcnow() + datetime.timedelta(hours=2),
        iat=datetime.datetime.utcnow(),
    )
    token = jwt.encode(payload, settings.JWT_SECRET, algorithm="HS256")

    return token


def update_user_profile(user: "User", user_id: int, user_data: "UserDataClass"):
    instance = get_object_or_404(models.User, pk=user_id)

    instance.first_name = user_data['first_name']
    instance.last_name = user_data['last_name']
    instance.username = user_data['username']
    instance.phone_number = user_data['phone_number']
    instance.country = user_data['country']
    instance.address = user_data['address']
    instance.postal_code = user_data['postal_code']

    instance.save()

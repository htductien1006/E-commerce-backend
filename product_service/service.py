import dataclasses
import datetime
import jwt
from rest_framework import exceptions
from typing import TYPE_CHECKING
from django.conf import settings
from django.shortcuts import get_object_or_404
from . import models
from user_service.models import ShoppingSession


@dataclasses.dataclass
class CardItemsDataClass:
    id: int
    quantity: int
    product_id: models.Product
    session_id: ShoppingSession = None

    @classmethod
    def from_instance(cls, cartitems: "CartItems") -> "CardItemsDataClass":
        return cls(
            id=cartitems.id,
            quantity=cartitems.quantity,
            product_id=cartitems.product_id,
            session_id=cartitems.session_id
        )


def create_payment_detail():
    instance = models.PaymentDetail()
    instance.save()
    data_respone = {
        "id": instance.id,
        "amount": instance.amount,
        "status": instance.status
    }
    return data_respone


def create_order_detail(user_id):
    payment_detail = create_payment_detail()
    payment_object = get_object_or_404(
        models.PaymentDetail, pk=payment_detail['id'])
    # shopping_session = get_object_or_404(
    #     "user_service.ShoppingSession", user_id=user_id)

    instance = models.OrderDetails(
        total=0, payment_id=payment_object, user_id=user_id)

    instance.save()
    pass


def add_order_item():

    return


def create_cart_item(cartitem_data: "CardItemsDataClass", user_id):
    shopping_session = get_object_or_404(ShoppingSession, user_id=user_id)
    product_instance = get_object_or_404(
        models.Product, pk=cartitem_data['product_id'])
    instance = models.CartItems(
        quantity=cartitem_data['quantity'], product_id=product_instance, session_id=shopping_session)
    instance.save()
    return {
        'id': instance.id,
        'quantity': instance.quantity,
        'product_id': {
            'id': instance.product_id.id,
        },
        'session_id': {
            'id': instance.session_id.id,
        }
    }


def update_cart_item(cart_id, quantity):
    instance = get_object_or_404(models.CartItems, pk=cart_id)
    instance.quantity = quantity
    instance.save()
    cart_response = {
        'id': instance.id,
        'quantity': instance.quantity,

    }
    return cart_response


def delete_cart_item(cart_id):
    instance = get_object_or_404(models.CartItems, pk=cart_id)
    instance.delete()
    return {'message': "Delete Cart Success"}

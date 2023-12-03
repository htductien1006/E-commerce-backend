import dataclasses
import datetime
import jwt
from rest_framework import exceptions
from typing import TYPE_CHECKING
from django.conf import settings
from django.shortcuts import get_object_or_404
from . import models
from user_service.models import ShoppingSession, User

# ------------------------------------Payment------------------------------


def create_payment_detail():
    instance = models.PaymentDetail(
        payment_type="VNPay", amount=0, status="Not Completed")
    instance.save()

    return instance


def update_payment_detail(payment_id, data_change):
    instance = get_object_or_404(models.PaymentDetail, pk=payment_id)
    if (data_change['payment_type']):
        instance.payment_type = data_change['payment_type']
    if (data_change['amount']):
        instance.amount = data_change['amount']
    if (data_change['status']):
        instance.status = data_change['status']
    instance.save()

    return


# ---------------------------------------Orderdetail---------------------------

def create_order_detail(shoppingsesion_data, user_id):
    user_detail = get_object_or_404(User, pk=user_id)
    instance = models.OrderDetails(
        total=0, payment_id=shoppingsesion_data.payment_id, user_id=user_detail)
    instance.save()
    cartitem_list = models.CartItems.objects.get(
        session_id=shoppingsesion_data)
    for cartitem in cartitem_list:
        order_item = models.OrderItems(
            quantity=cartitem.quantity, product_id=cartitem.product_id, order_id=instance)
        order_item.save()
    # return {
    #     "id": instance.id,
    #     "payment_id": {
    #         "id": instance.payment_id.id,
    #         "amount": instance.payment_id.amount,
    #         "status": instance.payment_id.status,
    #         "create_time": instance.payment_id.create_time
    #     },
    #     "user_id": {
    #         'id': instance.user_id.id,
    #         'name': instance.user_id.name
    #     }
    # }

# ----------------------------OrderItem-------------------------


def add_order_item(orderitem_data):
    product_instace = get_object_or_404(
        models.Product, pk=orderitem_data['id'])
    orderdetail_instance = get_object_or_404(
        models.Product, pk=orderitem_data['order_id'])
    instance = models.OrderItems(
        quantity=orderitem_data['quantity'], product_id=product_instace, order_id=orderdetail_instance)
    instance.save()
    instance_response = {
        'id': instance.id,
        'product_id': {
            'id': instance.product_id.id,
            'name': instance.product_id.name,
            'price': instance.product_id.price
        },
        'order_id': {
            'id': instance.order_id.id
        }

    }
    return instance_response


# ---------------------------CartItem-----------------------------------
def create_cart_item(cartitem_data, user_id):
    shopping_session = get_object_or_404(ShoppingSession, user_id=user_id)
    product_instance = get_object_or_404(
        models.Product, pk=cartitem_data['product_id'])
    instance = models.CartItems(
        quantity=cartitem_data['quantity'], product_id=product_instance, session_id=shopping_session)
    instance.save()
    shopping_session.total = shopping_session.total+1
    shopping_session.payment_id.amount = shopping_session.payment_id.amount + \
        cartitem_data.quantity*cartitem_data.product_id.price
    shopping_session.save()
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
    shopping_session = get_object_or_404(
        models.CartItems, pk=instance.session_id.id)
    shopping_session.payment_id.amount = shopping_session.payment_id.amount - \
        instance.quantity*instance.product_id.price
    instance.quantity = quantity
    instance.save()
    shopping_session.payment_id.amount = shopping_session.payment_id.amount + \
        instance.quantity*instance.product_id.price
    shopping_session.save()
    cart_response = {
        'id': instance.id,
        'quantity': instance.quantity,
    }
    return cart_response


def delete_cart_item(cart_id):
    instance = get_object_or_404(models.CartItems, pk=cart_id)
    shopping_session = get_object_or_404(
        models.CartItems, pk=instance.session_id.id)
    shopping_session.total = shopping_session.total-1
    shopping_session.payment_id.amount = shopping_session.payment_id.amount + \
        instance.quantity*instance.product_id.price
    instance.delete()
    return {'message': "Delete Cart Success"}

from django.shortcuts import get_object_or_404
from . import models
from email.message import EmailMessage
import ssl
import smtplib
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
    if (data_change['status']):
        instance.status = data_change['status']
    instance.save()
    payment_response = {
        "id": instance.id,
        "payment_type": instance.payment_type,
        "amount": instance.amount,
        "status": instance.status
    }

    return payment_response


# ---------------------------------------Orderdetail---------------------------

def create_order_detail(shoppingsesion_data, user_id):
    try:
        user_detail = get_object_or_404(User, pk=user_id)
        instance = models.OrderDetails(
            total=shoppingsesion_data.total, payment_id=shoppingsesion_data.payment_id, user_id=user_detail)
        instance.save()
        cartitem_list = models.CartItems.objects.filter(
            session_id=shoppingsesion_data)
        for cartitem in cartitem_list:
            order_item = models.OrderItems(
                quantity=cartitem.quantity, product_id=cartitem.product_id, order_id=instance)
            order_item.save()
    except:
        print("Order Detail has been created")


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
    shopping_session = ShoppingSession.objects.filter(user_id=user_id).first()
    payment_instance = get_object_or_404(
        models.PaymentDetail, pk=shopping_session.payment_id.id)
    product_instance = get_object_or_404(
        models.Product, pk=cartitem_data['product_id'])
    instance = models.CartItems(
        quantity=cartitem_data['quantity'], product_id=product_instance, session_id=shopping_session)
    instance.save()
    shopping_session.total = shopping_session.total+1
    payment_instance.amount = payment_instance.amount + \
        instance.quantity*instance.product_id.price
    shopping_session.save()
    payment_instance.save()
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
        ShoppingSession, pk=instance.session_id.id)
    payment_instance = get_object_or_404(
        models.PaymentDetail, pk=instance.session_id.id)
    payment_instance.amount = payment_instance.amount - \
        instance.quantity*instance.product_id.price
    instance.quantity = quantity
    payment_instance.amount = payment_instance.amount + \
        instance.quantity*instance.product_id.price
    instance.save()
    payment_instance.save()
    shopping_session.save()
    cart_response = {
        'id': instance.id,
        'quantity': instance.quantity,
    }
    return cart_response


def delete_cart_item(cart_id):
    instance = get_object_or_404(models.CartItems, pk=cart_id)
    shopping_session = get_object_or_404(
        ShoppingSession, pk=instance.session_id.id)
    payment_instance = get_object_or_404(
        models.PaymentDetail, pk=shopping_session.payment_id.id)
    shopping_session.total = shopping_session.total-1
    payment_instance.amount = payment_instance.amount - \
        instance.quantity*instance.product_id.price
    instance.delete()
    shopping_session.save()
    payment_instance.save()
    return {'message': "Delete Cart Success"}


def send_email(user_email):
    email_sender = 'souriquecorner@gmail.com'
    email_password = "qmwl baqz luzi rrhs"
    email_receiver = user_email

    subject = 'Your Order has been process!'

    body = """
    Dear Customer,

    Thank you for choosing our shop. We appreciate your business and would like to inform you that your order has been processed successfully. Our team is working diligently to prepare your items for shipment.

    Please note that the estimated delivery time for your order is a few days. However, please keep in mind that this is an estimate and actual delivery times may vary depending on various factors such as your location and any unforeseen circumstances.

    We understand that you are excited to receive your order, and we assure you that we are doing our best to fulfill it as quickly as possible. Once your order is shipped, we will provide you with a tracking number so that you can monitor its progress.

    If you have any questions or concerns regarding your order, please don't hesitate to reach out to our customer service team. We are here to assist you and provide any necessary updates.

    Thank you once again for choosing our shop. We value your business and look forward to delivering your order to you soon.

    Best regards,

    SouriqueCorner Shop
    """
    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subject
    em.set_content(body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())

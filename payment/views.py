from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from product_service import models, service
from payment.utils import make_paypal_payment, verify_paypal_payment
from user_service.models import ShoppingSession
from user_service import authentication

# Create your views here.


class MakePaymentAPI(APIView):
    """
    endpoint for create payment url
    """
    authentication_classes = (authentication.CustomUserAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        payment_id = request.data['payment_id']
        payment_instance = get_object_or_404(
            models.PaymentDetail, pk=payment_id)

        amount = round(payment_instance.amount / 23400, 2)

        status, paypal_id, approved_url = make_paypal_payment(
            amount=amount, currency="USD", return_url="https://example.com/payment/paypal/success/", cancel_url="https://example.com")

        if status:
            return Response({"success": True, "msg": "payment link has been successfully created", "approved_url": approved_url}, status=201)
        else:
            return Response({"success": False, "msg": "Authentication or payment failed"}, status=400)


class VerifyPaymentAPI(APIView):
    authentication_classes = (authentication.CustomUserAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        user = request.user
        paypal_id = request.data['paypal_id']
        payer_id = request.data['payer_id']
        paypal_payment_status = verify_paypal_payment(paypal_id, payer_id)

        if paypal_payment_status:
            service.send_email(user_email=user.email)
            return Response({"success": True, "msg": "payment improved"}, status=200)
        else:
            return Response({"success": False, "msg": "payment failed or cancelled"}, status=200)

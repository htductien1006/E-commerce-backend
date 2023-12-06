from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from product_service import models
from user_service.models import ShoppingSession
from payment.utils import make_paypal_payment, verify_paypal_payment

# Create your views here.
class MakePaymentAPI(APIView):
    """
    endpoint for create payment url
    """

    def post(self, request, *args, **kwargs):
        payment_id = request.data['payment_id']
        print(payment_id)
        payment_instance = get_object_or_404(
                models.PaymentDetail, pk=payment_id)

        
        amount = payment_instance.amount

        status,paypal_id,approved_url=make_paypal_payment(amount=amount,currency="USD",return_url="https://example.com/payment/paypal/success/",cancel_url="https://example.com")

        print(approved_url)

        if status:
            return Response({"success":True,"msg":"payment link has been successfully created","approved_url":approved_url},status=201)
        else:
            return Response({"success":False,"msg":"Authentication or payment failed"},status=400)
        

class VerifyPaymentAPI(APIView):
    def post(self, request, *args, **kwargs):
        paypal_id = request.data['paypal_id']
        payer_id = request.data['payer_id']
        print(paypal_id, payer_id)
        paypal_payment_status = verify_paypal_payment(paypal_id, payer_id)

        if paypal_payment_status:
            return Response({"success":True,"msg":"payment improved"},status=200)
        else:
            return Response({"success":False,"msg":"payment failed or cancelled"},status=200)
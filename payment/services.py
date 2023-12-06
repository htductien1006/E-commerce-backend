from django.shortcuts import get_object_or_404
from product_service import models
from user_service.models import ShoppingSession, User

def get_payment_amount(shoppingsession_data): 
    amount = shoppingsession_data.total
    payment_id = shoppingsession_data.payment_id
    
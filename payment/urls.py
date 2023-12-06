from django.urls import path
from . import views

urlpatterns = [
    path('checkout/', views.MakePaymentAPI.as_view(), name= 'createPayment'),
    path('verify/', views.VerifyPaymentAPI.as_view(), name= 'validatePayment'),
]
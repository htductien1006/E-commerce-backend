from django.urls import path, include
from api import views

urlpatterns = [
    path('users/', include('user_service.urls')),
    path('productservice/', include('product_service.urls')),
    path('payment/', include('paypal.standard.ipn.urls')),
]

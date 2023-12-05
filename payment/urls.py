from django.urls import path
from . import views

url_patterns = [
    path('create/order', views.CreateOrderViewRemote.as_view(), name= 'ordercreate'),
    path('capture/order', views.CaptureOrderView.as_view(), name= 'captureorder'),
    
]
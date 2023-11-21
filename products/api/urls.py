from django.urls import path
from products.api import views

urlpatterns = [
    path('', views.home, name="home"),
    path('products/', views.getProducts, name='getProducts'),
    path('products/<int:id>', views.getProduct, name='getProduct')
]

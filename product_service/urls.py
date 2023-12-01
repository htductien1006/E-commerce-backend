from django.urls import path

from . import apis

urlpatterns = [
    path("product/", apis.ProductApi.as_view(), name="product"),
    path("product/<int:product_id>/", apis.ProductDetailApi.as_view(), name="product_detail")
]

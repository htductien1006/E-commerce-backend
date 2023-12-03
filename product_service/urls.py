from django.urls import path

from . import apis

urlpatterns = [
    path("product/", apis.ProductApi.as_view(), name="product"),
    path("product/<int:product_id>/",
         apis.ProductDetailApi.as_view(), name="product_detail"),
    path("product/carditem", apis.AddCartItemsAPI.as_view(), name="carditem_add"),
    path("product/carditem/<int:cart_id>",
         apis.CartItemDetailAPI.as_view(), name="carditem_detail")
]

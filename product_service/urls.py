from django.urls import path

from . import apis

urlpatterns = [
    path("product/", apis.ProductApi.as_view(), name="product"),
    path("product/shoppingsession",
         apis.ShoppingSessionAPI.as_view(), name="shopping_session"),
    path("product/<int:product_id>/",
         apis.ProductDetailApi.as_view(), name="product_detail"),
    path("product/addcarditem/", apis.AddCartItemsAPI.as_view(), name="carditem_add"),
    path("product/carditem/", apis.CartItemAPI.as_view(), name="get_card_item"),
    path("product/carditem/<int:cart_id>/",
         apis.CartItemDetailAPI.as_view(), name="carditem_detail"),
    path("product/payment/<int:payment_id>",
         apis.PaymentDetailAPI.as_view(), name="payment_detail"),
    path("product/orderlist/", apis.OrderDetailListAPI.as_view(), name="list_order"),
    path("product/orderlist/<int:orderdetail_id>/",
         apis.OrderItemsAPI.as_view(), name="list_order_detail"),
    path("product/orderlist/<int:orderdetail_id>/<int:orderitem_id>/",
         apis.OrderItemsDetailAPI.as_view(), name="list_order_detail")
]

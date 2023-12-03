from rest_framework import views, response, exceptions, permissions
from . import serializers as product_service_serializer
from . import models as models
from django.shortcuts import get_object_or_404
from user_service import serializers as user_serializer
from user_service import authentication
from . import service

# -------------------------------------Product Fetch Api ---------------------------


class ProductApi(views.APIView):
    def get(self, request):
        product_list = models.Product.objects.all()
        list_result = [{'id': entry.id, 'name': entry.name, 'price': entry.price, 'image_url': entry.image_url, 'uom_name': entry.uom_name, 'uom_quantitive': entry.uom_quantitive}
                       for entry in product_list]

        return response.Response(data=list_result)


class ProductDetailApi(views.APIView):
    def get(self, request, product_id):
        product = get_object_or_404(models.Product, pk=product_id)
        product_response = {'id': product.id, 'name': product.name, 'description': product.description, 'price': product.price,
                            'image_url': product.image_url, 'uom_name': product.uom_name, 'uom_quantitive': product.uom_quantitive}
        return response.Response(data=product_response)


# --------------------------Session API----------

class OrderDetailAPI(views.APIView):
    def get(self, request, shopping_id):
        orderdetail_list = models.OrderDetails.objects.get(id=shopping_id)
        orderdetail_response = [{'total': entry.total, 'payment_id': entry.payment_id}
                                for entry in orderdetail_list]
        return response.Response(data=orderdetail_response)


class OrderItemsAPI(views.APIView):
    def post(self, request):
        product_id = request.data['id']
        quantity = request.data['quantity']

        return response.Response(data={})


# --------------------------------------------CartItem----------------------------
class AddCartItemsAPI(views.APIView):
    authentication_classes = (authentication.CustomUserAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        current_user = request.user
        res = service.create_cart_item(
            cartitem_data=request.data, user_id=current_user.id)
        print(res)
        return response.Response(data=res)


class CartItemDetailAPI(views.APIView):
    authentication_classes = (authentication.CustomUserAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, cart_id):
        cart_item = get_object_or_404(models.CartItems, pk=cart_id)
        cart_response = {
            "id": cart_item.id,
            "quantity": cart_item.quantity
        }
        return response.Response(data=cart_response)

    def put(self, request, cart_id):
        quantity_change = request.data['quantity']
        res = service.update_cart_item(
            cart_id=cart_id, quantity=quantity_change)
        return response.Response(data=res)

    def delete(self, request, cart_id):
        res = service.delete_cart_item(cart_id=cart_id)
        return response.Response(data=res)

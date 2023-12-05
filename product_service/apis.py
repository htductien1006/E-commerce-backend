from rest_framework import views, response, exceptions, permissions
from . import serializers as product_service_serializer
from . import models as models
from django.shortcuts import get_object_or_404
from user_service.models import ShoppingSession
from user_service import serializers as user_serializer
from user_service import authentication
from . import service

# -------------------------------------Product Fetch Api ---------------------------


class ProductApi(views.APIView):
    def get(self, request):
        product_list = models.Product.objects.all()
        list_result = [{'id': entry.id, 'name': entry.name, 'price': entry.price, 'image_url': entry.image_url, 'uom_name': entry.uom_name, 'uom_quantitive': entry.uom_quantitive, "category_id": {
            "id": entry.category_id.id,
            "name": entry.category_id.name,
        }}
            for entry in product_list]

        return response.Response(data=list_result)


class CategoryApi(views.APIView):
    def get(self, request, category_id):
        category = models.Category.objects.get(id=category_id)
        product_list = models.Product.objects.filter(category_id=category)
        list_result = [{'id': entry.id,  'image_url': entry.image_url, 'name': entry.name, }
                       for entry in product_list]
        return response.Response(data=list_result)


class ProductDetailApi(views.APIView):
    def get(self, request, product_id):
        product = get_object_or_404(models.Product, pk=product_id)
        product_response = {'id': product.id, 'name': product.name, 'description': product.description, 'price': product.price,
                            'image_url': product.image_url, 'uom_name': product.uom_name, 'uom_quantitive': product.uom_quantitive, "category_id": product.category_id.id, "category_name": product.category_id.name}
        return response.Response(data=product_response)


# --------------------------Session API----------------------

class OrderDetailListAPI(views.APIView):
    authentication_classes = (authentication.CustomUserAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, shopping_id):
        user = request.user
        orderdetail_list = models.Orderdetail.objects.filter(user_id=user)
        orderdetail_response = [{'total': entry.total, 'payment_amount': entry.payment_id.amount, 'status': entry.payment_id.status, }
                                for entry in orderdetail_list]
        return response.Response(data=orderdetail_response)


class OrderItemsAPI(views.APIView):
    authentication_classes = (authentication.CustomUserAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, orderdetail_id):
        orderitem_list = get_object_or_404(
            models.OrderItems, order_id=orderdetail_id)
        data_response = [{
            'id': orderitem.id,
            'quantity': orderitem.quantity,
            'product_id': {
                'id': orderitem.product_id.id,
                'name': orderitem.product_id.name,
                'price': orderitem.product_id.price,
                'uom_name': orderitem.product_id.uom_name,
                'uom_quantitive': orderitem.product_id.uom_quantitive
            }
        } for orderitem in orderitem_list]

        return response.Response(data=data_response)


class OrderItemsDetailAPI(views.APIView):
    authentication_classes = (authentication.CustomUserAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, orderitem_id):
        orderitem = get_object_or_404(models.OrderItems, pk=orderitem_id)
        data_response = {
            'id': orderitem.id,
            'quantity': orderitem.quantity,
            'product_id': {
                'id': orderitem.product_id.id,
                'name': orderitem.product_id.name,
                'price': orderitem.product_id.price,
                'uom_name': orderitem.product_id.uom_name,
                'uom_quantitive': orderitem.product_id.uom_quantitive
            }
        }

        return response.Response(data=data_response)


# --------------------------------------------CartItem----------------------------
class AddCartItemsAPI(views.APIView):
    authentication_classes = (authentication.CustomUserAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        current_user = request.user
        res = service.create_cart_item(
            cartitem_data=request.data, user_id=current_user.id)
        return response.Response(data=res)


class CartItemAPI(views.APIView):
    authentication_classes = (authentication.CustomUserAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        user = request.user
        shopping_session = get_object_or_404(ShoppingSession, user_id=user)
        cartitem_list = models.CartItems.objects.filter(
            session_id=shopping_session)
        data_response = [{
            'id': instance.id,
            'quantity': instance.quantity,
            'product_id': {
                'id': instance.product_id.id,
                'name': instance.product_id.name,
                'price': instance.product_id.price,
                'image_url': instance.product_id.image_url,
            }
        } for instance in cartitem_list]
        return response.Response(data=data_response)


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


# --------------------------------------------Payment----------------------------

class PaymentDetailAPI(views.APIView):
    authentication_classes = (authentication.CustomUserAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, payment_id):
        payment_item = get_object_or_404(models.PaymentDetail, pk=payment_id)
        payment_response = {
            "id": payment_item.id,
            "payment_type": payment_item.payment_type,
            "amount": payment_item.amount,
            "status": payment_item.status
        }
        return response.Response(data=payment_response)

    def put(self, request, payment_id):
        try:
            user = request.user
            payment_instance = get_object_or_404(
                models.PaymentDetail, pk=payment_id)
            shoppingsession_data = ShoppingSession.objects.get(
                payment_id=payment_instance)
            if request.data['status'] == "Completed":
                service.create_order_detail(
                    shoppingsesion_data=shoppingsession_data, user_id=user.id)
                shoppingsession_data.delete()
                payment = service.create_payment_detail()
                instance = ShoppingSession(
                    user_id=user, payment_id=payment, total=0)
                instance.save()
            data = {
                'payment_type': request.data['payment_type'],
                'status': request.data['status']
            }
            res = service.update_payment_detail(
                payment_id=payment_id, data_change=data)
            return response.Response(data=res)
        except:
            return response.Response(data={'message': "Shopping Session Has been Deleted or Can't Handle"})

# --------------------------------------------Shopping Session----------------------------


class ShoppingSessionAPI(views.APIView):
    authentication_classes = (authentication.CustomUserAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        try:
            currentuser = request.user
            shopping_session = ShoppingSession.objects.filter(
                user_id=currentuser).first()
            data_response = {
                "total": shopping_session.total,
                'payment_id': {
                    'id': shopping_session.payment_id.id
                }
            }
            return response.Response(data=data_response)
        except:
            return response.Response(data={'message': "Failed"})

from rest_framework import views, response, exceptions, permissions
# from . import serializers as product_service_serializer
from . import models as models
from django.shortcuts import get_object_or_404


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

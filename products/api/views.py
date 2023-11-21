from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from products.products import products

# Create your views here.
def home(request):
    return JsonResponse('Product API', safe=False)

@api_view(['GET'])
def getProducts(request):
    return Response(products)

@api_view(['GET'])
def getProduct(request, id):
    product = None

    for prod in products:
        if prod['id'] == id:
            product = prod
            break
    
    return Response(product)
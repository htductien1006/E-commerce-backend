from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class PaymentView(APIView):
    """
    endpoint for create payment url
    """

    def post(self, request, *args, **kwargs):
        
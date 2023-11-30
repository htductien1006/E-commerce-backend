from django.urls import path, include
from api import views

urlpatterns = [
    # path('products/', include('products.api.urls')),
    path('users/', include('user_service.urls'))
]

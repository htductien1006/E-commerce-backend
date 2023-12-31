from rest_framework import views, response, exceptions, permissions
from product_service import service
from . import models
from . import serializers as user_serializer
from . import services, authentication


class RegisterApi(views.APIView):
    def post(self, request):
        try:
            serializer = user_serializer.UserSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)

            data = serializer.validated_data

            serializer.instance = services.create_user(user_dc=data)

            return response.Response(data=serializer.data)
        except:
            return response.Response(data={'message': "Failed"})


class LoginApi(views.APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        try:
            email = request.data["email"]
            password = request.data["password"]

            user = services.user_email_selector(email)

            if user is None:
                raise exceptions.AuthenticationFailed("Invalid Credentials")

            if not user.check_password(raw_password=password):
                raise exceptions.AuthenticationFailed("Invalid Credentials")

            token = services.create_token(user=user, user_id=user.id)

            resp = response.Response(data={'token': token})

            resp.set_cookie(key="jwt", value=token, httponly=True)

            return resp
        except:
            return response.Response(data={'message': "Wrong Authetication"})


class UserApi(views.APIView):

    authentication_classes = (authentication.CustomUserAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        user = request.user
        serializer = user_serializer.UserProfileSerializer(user)

        return response.Response(serializer.data)

    def put(self, request):
        serializer = user_serializer.UserProfileSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user_profile = serializer.validated_data
        serializer.instance = services.update_user_profile(
            user=request.user, user_id=request.user.id, user_data=user_profile
        )

        return response.Response(data=serializer.data)


class LogoutApi(views.APIView):
    authentication_classes = (authentication.CustomUserAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        try:
            user = request.user
            resp = response.Response()
            try:
                check_session = models.ShoppingSession.objects.get(
                    user_id=user)
                if check_session:
                    service.create_order_detail(
                        shoppingsesion_data=check_session, user_id=user.id)
                    check_session.delete()
            except:
                print("Nothing At All")
            resp.delete_cookie("jwt")
            resp.data = {"message": "Good Bye"}

            return resp
        except:
            return response.Response(data={"message": "Good Bye"})

from django.urls import path

from . import apis

urlpatterns = [
    path("register/", apis.RegisterApi.as_view(), name="register"),
    path("login/", apis.LoginApi.as_view(), name="login"),
    path("profile/", apis.UserApi.as_view(), name="profile"),
    # path("profile/update", apis.UserUpdateInfoApi.as_view(), name="update_profile"),
    path("logout/", apis.LogoutApi.as_view(), name="logout"),
]

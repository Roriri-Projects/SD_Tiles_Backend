from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import LoginView, RegisterView, LogoutView, GetAuthUserDetails,UserDetailAPIView

app_name = "access"

urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("register/", RegisterView.as_view(), name="register"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("user/details/", GetAuthUserDetails.as_view(), name="user_details"),
    path("user/update/", UserDetailAPIView.as_view(), name="user_update"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]

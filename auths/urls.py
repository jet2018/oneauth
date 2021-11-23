from django.urls import path
from .views import (
    CheckEmailOrUsernameOrPhone,
    Check_User_Password,
    Error_Unknown_Token,
    SplashScreen,
    authorize
)

app_name = 'auths'
urlpatterns = [
    path("", SplashScreen.as_view(), name="splash"),
    path("<sec_key>/authorize", authorize, name="authorise"),
    path("login/", Check_User_Password, name="login"),
    path("check_credentials/", CheckEmailOrUsernameOrPhone, name="checker"),
    path("check_password/<username>/", Check_User_Password, name="check_pwd"),
    path("errors/unknown_referrer/", Error_Unknown_Token.as_view(), name="unknown_token"),
]
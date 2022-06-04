from django.urls import path
from .views import SignUp, Profile, LogIn, LogOut, ResetPassword, ResetPasswordConfirm

app_name = "accounts"
urlpatterns = [
    path("register/", SignUp.as_view(), name="register"),
    path("profile/", Profile.as_view(), name="profile"),
    path("login/", LogIn.as_view(), name="login"),
    path("logout/", LogOut.as_view(), name="logout"),
    path("reset_password/", ResetPassword.as_view(), name="reset_password"),
    path(
        "reset_password_confirm/$<uidb64>/<token>/",
        ResetPasswordConfirm.as_view(),
        name="reset_password_confirm",
    ),
]

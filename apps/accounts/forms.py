from django.contrib.auth.forms import (
    UserCreationForm,
    UserChangeForm,
)
from django.contrib.auth import get_user_model

User = get_user_model()


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")


class ProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "first_name",
            "last_name",
        )

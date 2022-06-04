from django.forms import EmailField
from django.contrib.auth.forms import (
    UserCreationForm,
    UsernameField,
)
from django.contrib.auth import get_user_model

User = get_user_model()


class CreationForm(UserCreationForm):
    """
    A form that creates a user, with no privileges, from the given username, email and
    password.
    """

    class Meta:
        model = User
        fields = ("username", "email")
        field_classes = {"username": UsernameField, "email": EmailField}

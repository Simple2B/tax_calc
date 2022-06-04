from django.urls import path
from .views import transfer

app_name = "taxes"

urlpatterns = [
    path("transfer", transfer, name="transfer"),
]

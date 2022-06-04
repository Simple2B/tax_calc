from django.urls import path
from .views import upload, transactions

app_name = "transactions"

urlpatterns = [
    path("upload/", upload, name="upload"),
    path("", transactions, name="list"),
]

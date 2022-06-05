from django.urls import path
from .views import TransactionsUpload, transactions

app_name = "transactions"

urlpatterns = [
    path("upload/", TransactionsUpload.as_view(), name="upload"),
    path("", transactions, name="list"),
]

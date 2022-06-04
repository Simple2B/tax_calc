from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.core.paginator import Paginator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.urls import reverse_lazy, reverse
from django.contrib.auth.decorators import login_required
import pandas as pd
from .models import Transaction
from apps.countries.models import Country
from .forms import UploadFileForm

User = get_user_model()


@login_required
def transactions(request):
    transactions = Transaction.objects.filter(user=request.user)
    paginator = Paginator(transactions, 50)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {
        "count": len(transactions),
        "headers": [
            "UNIQUE_ACCOUNT_IDENTIFIER",
            "ACTIVITY_PERIOD",
            "SALES_CHANNEL",
            "MARKETPLACE",
        ],
        "data": page_obj,
    }
    return render(request, "transaction/list.html", context)


class TransactionDetail(LoginRequiredMixin, DetailView):
    model = Transaction


@login_required
def upload(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            df = pd.read_csv(
                request.FILES["file"],
                dtype=object,
            ).fillna(0)
            for index, row in df.iterrows():
                obj = {k.lower(): v for k, v in row.to_dict().items()}
                obj["user"] = User.objects.get(id=request.user.id)
                obj["activity_period"] = pd.to_datetime(
                    obj.get("activity_period")
                ).date()
                obj["tax_calculation_date"] = pd.to_datetime(
                    obj.get("tax_calculation_date")
                ).date()
                obj["transaction_depart_date"] = pd.to_datetime(
                    obj.get("transaction_depart_date")
                ).date()
                obj["transaction_arrival_date"] = pd.to_datetime(
                    obj.get("transaction_arrival_date")
                ).date()
                obj["transaction_complete_date"] = pd.to_datetime(
                    obj.get("transaction_complete_date")
                ).date()
                obj["vat_inv_exchange_rate_date"] = pd.to_datetime(
                    obj.get("vat_inv_exchange_rate_date")
                ).date()
                try:
                    transaction = Transaction(**obj)
                    transaction.save()
                    transaction.full_clean()
                except:
                    messages.success(
                        request, "Failed in transaction".format(transaction)
                    )
            messages.success(request, "File posted successfully")
            return True
        else:
            return render(request, "transaction/upload.html", {"form": form})
    else:
        form = UploadFileForm()
        return render(request, "transaction/upload.html", {"form": form})


class TransactionUpdate(LoginRequiredMixin, UpdateView):
    model = Transaction

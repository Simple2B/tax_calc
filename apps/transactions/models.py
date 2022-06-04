from django.db import models
from django.db.models.deletion import CASCADE, DO_NOTHING
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

from apps.countries.models import Country

User = get_user_model()


class Transaction(models.Model):
    class SalesChannel(models.TextChoices):
        AFN = "AFN"
        UNDEFINED = "N/A"

    class ProgramType(models.TextChoices):
        REGULAR = "REGULAR"
        UNDEFINED = "N/A"

    class TransactionType(models.TextChoices):
        SALE = "SALE"
        REFUND = "REFUND"
        FC_TRANSFER = "FC_TRANSFER"
        UNDEFINED = "N/A"

    class TransactionCurrencyCode(models.TextChoices):
        EUR = "EUR"
        GBP = "GBP"
        UNDEFINED = "N/A"

    class ProductTaxCode(models.TextChoices):
        A_GEN_STANDARD = "A_GEN_STANDARD"
        UNDEFINED = "N/A"

    class TransactionMode(models.TextChoices):
        CONSIGNMENT_BY_POST = "CONSIGNMENT_BY_POST"
        TRANSPORT_BY_ROAD = "TRANSPORT_BY_ROAD"
        UNDEFINED = "N/A"

    class DeliveryConditions(models.TextChoices):
        DAP = "DAP"
        UNDEFINED = "N/A"

    class TaxableJurisdictionLevel(models.TextChoices):
        COUNTRY = "Country"
        UNDEFINED = "N/A"

    class ExportOutsideEu(models.TextChoices):
        YES = "YES"
        NO = "NO"
        UNDEFINED = "N/A"

    class TaxReportingScheme(models.TextChoices):
        DEEMED_RESELLER = "DEEMED_RESELLER"
        REGULAR = "REGULAR"
        UNDEFINED = "N/A"

    class TaxCollectionResponsibility(models.TextChoices):
        MARKETPLACE = "MARKETPLACE"
        SELLER = "SELLER"
        UNDEFINED = "N/A"

    user = models.ForeignKey(User, on_delete=CASCADE)
    unique_account_identifier = models.CharField(
        max_length=16, editable=False, null=False, blank=False
    )
    activity_period = models.DateField(editable=False, null=False, blank=False)
    sales_channel = models.CharField(max_length=8, choices=SalesChannel.choices)
    # marketplace = models.ForeignKey(Country, on_delete=DO_NOTHING)
    marketplace = models.CharField(max_length=32, null=True, blank=True)
    program_type = models.CharField(max_length=16, choices=ProgramType.choices)
    transaction_type = models.CharField(max_length=16, choices=TransactionType.choices)
    transaction_event_id = models.CharField(max_length=32)
    activity_transaction_id = models.CharField(max_length=32)
    tax_calculation_date = models.DateField(null=True, blank=True)
    transaction_depart_date = models.DateField(null=True, blank=True)
    transaction_arrival_date = models.DateField(null=True, blank=True)
    transaction_complete_date = models.DateField(null=True, blank=True)
    seller_sku = models.CharField(max_length=16, null=True, blank=True)
    asin = models.CharField(max_length=16, null=True, blank=True)
    item_description = models.TextField(max_length=1024, null=True, blank=True)
    item_manufacture_country = models.CharField(max_length=16, null=True, blank=True)
    qty = models.IntegerField(null=True, blank=True)
    item_weight = models.FloatField(null=True, blank=True)
    total_activity_weight = models.FloatField(null=True, blank=True)
    cost_price_of_items = models.FloatField(null=True, blank=True)
    price_of_items_amt_vat_excl = models.FloatField(null=True, blank=True)
    promo_price_of_items_amt_vat_excl = models.FloatField(null=True, blank=True)
    total_price_of_items_amt_vat_excl = models.FloatField(null=True, blank=True)
    ship_charge_amt_vat_excl = models.FloatField(null=True, blank=True)
    promo_ship_charge_amt_vat_excl = models.FloatField(null=True, blank=True)
    total_ship_charge_amt_vat_excl = models.FloatField(null=True, blank=True)
    gift_wrap_amt_vat_excl = models.FloatField(null=True, blank=True)
    promo_gift_wrap_amt_vat_excl = models.FloatField(null=True, blank=True)
    total_gift_wrap_amt_vat_excl = models.FloatField(null=True, blank=True)
    total_activity_value_amt_vat_excl = models.FloatField(null=True, blank=True)
    price_of_items_vat_rate_percent = models.FloatField(null=True, blank=True)
    price_of_items_vat_amt = models.FloatField(null=True, blank=True)
    promo_price_of_items_vat_amt = models.FloatField(null=True, blank=True)
    total_price_of_items_vat_amt = models.FloatField(null=True, blank=True)
    ship_charge_vat_rate_percent = models.FloatField(null=True, blank=True)
    ship_charge_vat_amt = models.FloatField(null=True, blank=True)
    promo_ship_charge_vat_amt = models.FloatField(null=True, blank=True)
    total_ship_charge_vat_amt = models.FloatField(null=True, blank=True)
    gift_wrap_vat_rate_percent = models.FloatField(null=True, blank=True)
    gift_wrap_vat_amt = models.FloatField(null=True, blank=True)
    promo_gift_wrap_vat_amt = models.FloatField(null=True, blank=True)
    total_gift_wrap_vat_amt = models.FloatField(null=True, blank=True)
    total_activity_value_vat_amt = models.FloatField(null=True, blank=True)
    price_of_items_amt_vat_incl = models.FloatField(null=True, blank=True)
    promo_price_of_items_amt_vat_incl = models.FloatField(null=True, blank=True)
    total_price_of_items_amt_vat_incl = models.FloatField(null=True, blank=True)
    ship_charge_amt_vat_incl = models.FloatField(null=True, blank=True)
    promo_ship_charge_amt_vat_incl = models.FloatField(null=True, blank=True)
    total_ship_charge_amt_vat_incl = models.FloatField(null=True, blank=True)
    gift_wrap_amt_vat_incl = models.FloatField(null=True, blank=True)
    promo_gift_wrap_amt_vat_incl = models.FloatField(null=True, blank=True)
    total_gift_wrap_amt_vat_incl = models.FloatField(null=True, blank=True)
    total_activity_value_amt_vat_incl = models.FloatField(null=True, blank=True)
    transaction_currency_code = models.CharField(
        max_length=4, choices=TransactionCurrencyCode.choices
    )
    commodity_code = models.CharField(max_length=64, null=True, blank=True)
    statistical_code_depart = models.CharField(max_length=64, null=True, blank=True)
    statistical_code_arrival = models.CharField(max_length=64, null=True, blank=True)
    commodity_code_supplementary_unit = models.CharField(
        max_length=64, null=True, blank=True
    )
    item_qty_supplementary_unit = models.CharField(max_length=64, null=True, blank=True)
    total_activity_supplementary_unit = models.CharField(
        max_length=64, null=True, blank=True
    )
    product_tax_code = models.CharField(max_length=32, choices=ProductTaxCode.choices)
    depature_city = models.CharField(max_length=64, null=True, blank=True)
    departure_country = models.CharField(max_length=8, null=True, blank=True)
    departure_post_code = models.CharField(max_length=16, null=True, blank=True)
    arrival_city = models.CharField(max_length=64, null=True, blank=True)
    arrival_country = models.CharField(max_length=8, null=True, blank=True)
    arrival_post_code = models.CharField(max_length=16, null=True, blank=True)
    sale_depart_country = models.CharField(max_length=8, null=True, blank=True)
    sale_arrival_country = models.CharField(max_length=8, null=True, blank=True)
    transportation_mode = models.CharField(
        max_length=32, choices=TransactionMode.choices
    )
    delivery_conditions = models.CharField(
        max_length=8, choices=DeliveryConditions.choices
    )
    seller_depart_vat_number_country = models.CharField(
        max_length=8, null=True, blank=True
    )
    seller_depart_country_vat_number = models.CharField(
        max_length=16, null=True, blank=True
    )
    seller_arrival_vat_number_country = models.CharField(
        max_length=8, null=True, blank=True
    )
    seller_arrival_country_vat_number = models.CharField(
        max_length=16, null=True, blank=True
    )
    transaction_seller_vat_number_country = models.CharField(
        max_length=8, null=True, blank=True
    )
    transaction_seller_vat_number = models.CharField(
        max_length=16, null=True, blank=True
    )
    buyer_vat_number_country = models.CharField(max_length=8, null=True, blank=True)
    buyer_vat_number = models.CharField(max_length=16, null=True, blank=True)
    vat_calculation_imputation_country = models.CharField(
        max_length=8, null=True, blank=True
    )
    taxable_jurisdiction = models.CharField(max_length=16, null=True, blank=True)
    taxable_jurisdiction_level = models.CharField(
        max_length=8, choices=TaxableJurisdictionLevel.choices
    )
    vat_inv_number = models.CharField(max_length=32, null=True, blank=True)
    vat_inv_converted_amt = models.FloatField(null=True, blank=True)
    vat_inv_currency_code = models.CharField(max_length=8, null=True, blank=True)
    vat_inv_exchange_rate = models.FloatField(null=True, blank=True)
    vat_inv_exchange_rate_date = models.DateField(null=True, blank=True)
    export_outside_eu = models.CharField(max_length=8, choices=ExportOutsideEu.choices)
    invoice_url = models.URLField(max_length=1024, null=True, blank=True)
    buyer_name = models.CharField(max_length=128, null=True, blank=True)
    arrival_address = models.CharField(max_length=128, null=True, blank=True)
    supplier_name = models.CharField(max_length=128, null=True, blank=True)
    supplier_vat_number = models.CharField(max_length=64, null=True, blank=True)
    tax_reporting_scheme = models.CharField(
        max_length=32, choices=TaxReportingScheme.choices
    )
    tax_collection_responsibility = models.CharField(
        max_length=32, choices=TaxCollectionResponsibility.choices
    )

    class Meta:
        verbose_name = "transaction"
        verbose_name_plural = "transactions"

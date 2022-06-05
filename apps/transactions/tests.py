import csv, os
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()
header = (
    "unique_account_identifier",
    "activity_period",
    "sales_channel",
    "marketplace",
    "program_type",
    "transaction_type",
    "transaction_event_id",
    "activity_transaction_id",
    "tax_calculation_date",
    "transaction_depart_date",
    "transaction_arrival_date",
    "transaction_complete_date",
    "seller_sku",
    "asin",
    "item_description",
    "item_manufacture_country",
    "qty",
    "item_weight",
    "total_activity_weight",
    "cost_price_of_items",
    "price_of_items_amt_vat_excl",
    "promo_price_of_items_amt_vat_excl",
    "total_price_of_items_amt_vat_excl",
    "ship_charge_amt_vat_excl",
    "promo_ship_charge_amt_vat_excl",
    "total_ship_charge_amt_vat_excl",
    "gift_wrap_amt_vat_excl",
    "promo_gift_wrap_amt_vat_excl",
    "total_gift_wrap_amt_vat_excl",
    "total_activity_value_amt_vat_excl",
    "price_of_items_vat_rate_percent",
    "price_of_items_vat_amt",
    "promo_price_of_items_vat_amt",
    "total_price_of_items_vat_amt",
    "ship_charge_vat_rate_percent",
    "ship_charge_vat_amt",
    "promo_ship_charge_vat_amt",
    "total_ship_charge_vat_amt",
    "gift_wrap_vat_rate_percent",
    "gift_wrap_vat_amt",
    "promo_gift_wrap_vat_amt",
    "total_gift_wrap_vat_amt",
    "total_activity_value_vat_amt",
    "price_of_items_amt_vat_incl",
    "promo_price_of_items_amt_vat_incl",
    "total_price_of_items_amt_vat_incl",
    "ship_charge_amt_vat_incl",
    "promo_ship_charge_amt_vat_incl",
    "total_ship_charge_amt_vat_incl",
    "gift_wrap_amt_vat_incl",
    "promo_gift_wrap_amt_vat_incl",
    "total_gift_wrap_amt_vat_incl",
    "total_activity_value_amt_vat_incl",
    "transaction_currency_code",
    "commodity_code",
    "statistical_code_depart",
    "statistical_code_arrival",
    "commodity_code_supplementary_unit",
    "item_qty_supplementary_unit",
    "total_activity_supplementary_unit",
    "product_tax_code",
    "depature_city",
    "departure_country",
    "departure_post_code",
    "arrival_city",
    "arrival_country",
    "arrival_post_code",
    "sale_depart_country",
    "sale_arrival_country",
    "transportation_mode",
    "delivery_conditions",
    "seller_depart_vat_number_country",
    "seller_depart_country_vat_number",
    "seller_arrival_vat_number_country",
    "seller_arrival_country_vat_number",
    "transaction_seller_vat_number_country",
    "transaction_seller_vat_number",
    "buyer_vat_number_country",
    "buyer_vat_number",
    "vat_calculation_imputation_country",
    "taxable_jurisdiction",
    "taxable_jurisdiction_level",
    "vat_inv_number",
    "vat_inv_converted_amt",
    "vat_inv_currency_code",
    "vat_inv_exchange_rate",
    "vat_inv_exchange_rate_date",
    "export_outside_eu",
    "invoice_url",
    "buyer_name",
    "arrival_address",
    "supplier_name",
    "supplier_vat_number",
    "tax_reporting_scheme",
    "tax_collection_responsibility",
)
test_data = (
    "A1B06KL11BH2B6",
    "2022-APR",
    "AFN",
    "amazon.es",
    "REGULAR",
    "SALE",
    "408-9088634-5664315",
    "DXcD9RpQp",
    "30-04-2022",
    "30-04-2022",
    "",
    "30-04-2022",
    "QP-AI71-THT0",
    "B01KHC5R0I",
    "Sports Stable Inflador Balones ",
    "",
    "1",
    "0.13",
    "0.13",
    "",
    "10.32",
    "",
    "10.32",
    "0.0",
    "",
    "0.0",
    "",
    "",
    "",
    "10.32",
    "0.0",
    "0.0",
    "",
    "0.0",
    "0.0",
    "0.0",
    "",
    "0.0",
    "",
    "",
    "",
    "",
    "0.0",
    "10.32",
    "",
    "10.32",
    "0.0",
    "",
    "0.0",
    "",
    "",
    "",
    "10.32",
    "EUR",
    "",
    "",
    "",
    "",
    "",
    "",
    "A_GEN_STANDARD",
    "Kolbaskowo",
    "PL",
    "72-001",
    "Guadalajara",
    "ES",
    "19005",
    "PL",
    "ES",
    "CONSIGNMENT_BY_POST",
    "DAP",
    "PL",
    "PL5263227212",
    "",
    "",
    "PL",
    "PL5263227212",
    "",
    "",
    "ES",
    "POLAND",
    "Country",
    "DS-INV-PL-163216811-2022-4684",
    "0.0",
    "PLN",
    "4.678",
    "28-04-2022",
    "NO",
    "https://www.Amazon.es/gp/invoice/download.html?v=urn%3aalx%3adoc%3a9d8cab0f-1f96-4462-8642-ace99a371392%3a89d6f357-a2c4-4cf2-8adc-ee1493e13634&t=EU_Retail_Forward",
    "",
    "",
    "",
    "",
    "DEEMED_RESELLER",
    "MARKETPLACE",
)


class UserMixin(object):
    @staticmethod
    def _create_user(user_number: int):
        user = User.objects.create(
            username=f"test{user_number}",
            email=f"test{user_number}@example.com",
            first_name=f"Name{user_number}",
            last_name=f"Lname{user_number}",
            is_active=True,
        )
        user.set_password(f"testPassword")
        user.save()
        return user


class TestImportFile(TestCase, UserMixin):
    def generate_file(self):
        try:
            file = open("test.csv", "w")
            wr = csv.writer(file)
            wr.writerow(header)
            wr.writerow(test_data)
        finally:
            file.close()

        return file

    def setUp(self) -> None:
        self.user = self._create_user(user_number=1)

        self.login_url = reverse("accounts:login")
        self.upload_url = reverse("transactions:upload")

    def login_user(self, username="test", password="testPassword"):
        response = self.client.post(
            self.login_url, {"username": username, "password": password}
        )
        return response

    def test_csv_importers(self):
        response = self.login_user(username=self.user.username)
        self.assertTrue(response)
        file = self.generate_file()
        file_path = file.name
        f = open(file_path, "r")

        result = self.client.post(self.upload_url, {"file": f})

        self.assertTrue(result.status_code, 200)
        os.remove(file.name)

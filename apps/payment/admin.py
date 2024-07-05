from django.contrib import admin

from .models import CreditCard, ElectronicBankTransfer, Payment


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ("id", "status", "amount", "created_at", "updated_at")
    search_fields = ("status", "amount")


@admin.register(CreditCard)
class CreditCardAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name_on_card",
        "card_number",
        "billing_address",
        "created_at",
        "updated_at",
    )
    search_fields = (
        "name_on_card",
        "card_number",
        "billing_address__street_address",
    )


@admin.register(ElectronicBankTransfer)
class ElectronicBankTransferAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "bank_name",
        "routing_number",
        "account_number",
        "created_at",
        "updated_at",
    )
    search_fields = ("bank_name", "routing_number", "account_number")

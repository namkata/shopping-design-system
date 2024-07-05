from django.contrib import admin

from .models import Shipment


@admin.register(Shipment)
class ShipmentAdmin(admin.ModelAdmin):
    list_display = [
        "order",
        "shipment_date",
        "estimated_arrival",
        "shipment_method",
        "status",
    ]
    list_filter = ["status", "shipment_date"]
    search_fields = ["order__id", "shipment_method"]

from apps.core.models import AuditModel, TimeStampedModel
from apps.order.models import Order
from django.db import models


class ShipmentStatus(models.TextChoices):
    PENDING = "Pending"
    SHIPPED = "Shipped"
    DELIVERED = "Delivered"
    ON_HOLD = "OnHold"


class Shipment(TimeStampedModel, AuditModel):
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    shipment_date = models.DateTimeField()
    estimated_arrival = models.DateTimeField()
    shipment_method = models.CharField(max_length=255)
    status = models.CharField(
        max_length=20,
        choices=ShipmentStatus.choices,
        default=ShipmentStatus.PENDING,
    )

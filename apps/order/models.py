from django.db import models

from apps.account.models import User
from apps.cart.models import Product
from apps.core.models import TimeStampedModel, AuditModel
from apps.payment.models import Payment


class OrderStatus(models.TextChoices):
    UNPAID = 'Unpaid'
    PENDING = 'Pending'
    COMPLETED = 'Completed'
    FAILED = 'Failed'
    DECLINED = 'Declined'
    CANCELED = 'Canceled'
    ABANDONED = 'Abandoned'
    SETTLING = 'Settling'
    SETTLED = 'Settled'
    REFUNDED = 'Refunded'


class Order(TimeStampedModel, AuditModel):
    order_number = models.CharField(max_length=255)
    status = models.CharField(max_length=20, choices=OrderStatus.choices, default=OrderStatus.PENDING)
    order_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE)
    items = models.ManyToManyField(Product, through='OrderItem')

    def __str__(self):
        return self.order_number


class OrderItem(TimeStampedModel, AuditModel):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.product.name} ({self.quantity})"

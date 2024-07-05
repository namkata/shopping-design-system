from django.db import models

from apps.account.models import Address
from apps.core.models import TimeStampedModel, AuditModel


class PaymentStatus(models.TextChoices):
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


class Payment(TimeStampedModel, AuditModel):
    status = models.CharField(max_length=20, choices=PaymentStatus.choices, default=PaymentStatus.UNPAID)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Payment of {self.amount} - {self.status}"


class CreditCard(TimeStampedModel, AuditModel):
    name_on_card = models.CharField(max_length=255)
    card_number = models.CharField(max_length=20)
    code = models.IntegerField()
    billing_address = models.OneToOneField(Address, on_delete=models.CASCADE)

    def __str__(self):
        return f"Credit Card ending in {self.card_number[-4:]}"


class ElectronicBankTransfer(TimeStampedModel, AuditModel):
    bank_name = models.CharField(max_length=255)
    routing_number = models.CharField(max_length=20)
    account_number = models.CharField(max_length=20)

    def __str__(self):
        return f"Bank Transfer from {self.bank_name}"
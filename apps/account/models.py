from apps.core.models import AuditModel, TimeStampedModel
from django.contrib.auth.models import AbstractUser
from django.db import models


class AccountStatus(models.TextChoices):
    ACTIVE = "Active"
    BLOCKED = "Blocked"
    BANNED = "Banned"
    COMPROMISED = "Compromised"
    ARCHIVED = "Archived"
    UNKNOWN = "Unknown"


class Address(TimeStampedModel, AuditModel):
    street_address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=20)
    country = models.CharField(max_length=100)


class User(AbstractUser, TimeStampedModel, AuditModel):
    address = models.OneToOneField(
        Address, on_delete=models.SET_NULL, null=True, blank=True
    )
    status = models.CharField(
        max_length=20,
        choices=AccountStatus.choices,
        default=AccountStatus.ACTIVE,
    )
    phone = models.CharField(max_length=20, blank=True, null=True)

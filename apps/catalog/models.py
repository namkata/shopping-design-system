from django.db import models

from apps.core.models import TimeStampedModel, AuditModel


class Catalog(TimeStampedModel, AuditModel):
    last_updated = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
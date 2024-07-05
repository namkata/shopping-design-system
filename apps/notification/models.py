from django.db import models

from apps.core.models import TimeStampedModel, AuditModel


class Notification(TimeStampedModel, AuditModel):
    notification_id = models.AutoField(primary_key=True)
    created_on = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    sent = models.BooleanField(default=False)

    class Meta:
        abstract = True


class SMSNotification(Notification):
    phone = models.CharField(max_length=20)


class EmailNotification(Notification):
    email = models.EmailField()

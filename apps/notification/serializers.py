from rest_framework import serializers

from .models import EmailNotification, SMSNotification


class SMSNotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = SMSNotification
        fields = "__all__"


class EmailNotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailNotification
        fields = "__all__"

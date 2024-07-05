from django.contrib import admin
from .models import SMSNotification, EmailNotification


@admin.register(SMSNotification)
class SMSNotificationAdmin(admin.ModelAdmin):
    list_display = ('notification_id', 'created_on', 'phone', 'sent', 'created_at', 'updated_at')
    search_fields = ('phone', 'content')


@admin.register(EmailNotification)
class EmailNotificationAdmin(admin.ModelAdmin):
    list_display = ('notification_id', 'created_on', 'email', 'sent', 'created_at', 'updated_at')
    search_fields = ('email', 'content')

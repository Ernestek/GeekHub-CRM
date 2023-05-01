from django.contrib import admin

from notifications.models import Notification


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at',)
# Register your models here.

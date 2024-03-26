from django.contrib import admin
from .models import AccountNotification

@admin.register(AccountNotification)
class AccountNotificationAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'is_active')
    list_filter = ('is_active', 'created_at')
    search_fields = ('title', 'message')

from django.contrib import admin
from .models import CustomerServiceMessage

@admin.register(CustomerServiceMessage)
class CustomerServiceMessageAdmin(admin.ModelAdmin):
    list_display = ('user', 'subject', 'created_at')

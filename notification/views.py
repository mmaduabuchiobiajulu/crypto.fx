from django.shortcuts import render
from .models import AccountNotification

def notifications(request):
    active_notifications = AccountNotification.objects.filter(is_active=True).order_by('-created_at')
    return render(request, 'notification/notifications.html', {'notifications': active_notifications})

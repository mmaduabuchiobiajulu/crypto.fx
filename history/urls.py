from django.urls import path
from .views import transaction_history

urlpatterns = [
    path('history/', transaction_history, name='transaction_history'),
]

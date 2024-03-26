from django.urls import path
from .views import customer_service_message_view, success_message_view

urlpatterns = [
    path('contact/', customer_service_message_view, name='contact'),
    path('contact/success/', success_message_view, name='success_message'),
]

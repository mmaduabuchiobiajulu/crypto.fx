from django.urls import path
from . import views

urlpatterns = [
    path('request/', views.withdrawal_request, name='withdrawal_request'),
    path('success/', views.withdrawal_success, name='withdrawal_success'),
]


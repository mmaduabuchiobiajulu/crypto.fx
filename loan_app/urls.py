from django.urls import path
from .views import apply_for_loan, application_success

urlpatterns = [
    path('apply/', apply_for_loan, name='apply_for_loan'),
    path('success/',application_success, name='application_success'),
]

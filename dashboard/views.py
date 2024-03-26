from django.shortcuts import render
from .models import MainBalance, LoanBalance
from django.utils import timezone
from datetime import timedelta

def dashboard_view(request):
    user = request.user
    try:
        main_balance = MainBalance.objects.get(user=user)
        loan_balance = LoanBalance.objects.get(user=user)
    except (MainBalance.DoesNotExist, LoanBalance.DoesNotExist):
        main_balance = None
        loan_balance = None

    # Calculate progress for the 168-hour (7 days) timeline
    current_time = timezone.now()
    end_time = current_time + timedelta(hours=168)
    progress = ((current_time - end_time).total_seconds() / (168 * 3600)) * 100

    context = {
        'main_balance': main_balance,
        'loan_balance': loan_balance,
        'progress': progress,
    }
    return render(request, 'dashboard/user_dashboard.html', context)

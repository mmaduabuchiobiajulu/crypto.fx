from django.shortcuts import render
from .models import Transaction

def transaction_history(request):
    transactions = Transaction.objects.filter(user=request.user).order_by('-timestamp')
    return render(request, 'transactions/history.html', {'transactions': transactions})

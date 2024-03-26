from django.shortcuts import render, redirect
from .forms import WithdrawalRequestForm
from django.contrib.auth.decorators import login_required

@login_required
def withdrawal_request(request):
    if request.method == 'POST':
        form = WithdrawalRequestForm(request.POST)
        if form.is_valid():
            withdrawal = form.save(commit=False)
            withdrawal.user = request.user
            withdrawal.save()
            return redirect('withdrawal_success')
    else:
        form = WithdrawalRequestForm()
    return render(request, 'finances/withdrawal_request.html', {'form': form})

def withdrawal_success(request):
    return render(request, 'finances/withdrawal_success.html')

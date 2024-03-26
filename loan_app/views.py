from django.shortcuts import render, redirect

from .forms import LoanApplicationForm


def apply_for_loan(request):
    if request.method == 'POST':
        form = LoanApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to a new URL:
            return redirect('application_success')
    else:
        form = LoanApplicationForm()

    return render(request, 'loan_app/apply.html', {'form': form})



def application_success(request):
    return render(request, 'loan_app/successethereum.html')




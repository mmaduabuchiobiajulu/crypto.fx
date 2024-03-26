from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import CustomerServiceMessageForm

@login_required
def customer_service_message_view(request):
    if request.method == 'POST':
        form = CustomerServiceMessageForm(request.POST)
        if form.is_valid():
            service_message = form.save(commit=False)
            service_message.user = request.user
            service_message.save()
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('success_message')
    else:
        form = CustomerServiceMessageForm()
    return render(request, 'CustomerServiceMessage/customer_service_message.html', {'form': form})

def success_message_view(request):
    return render(request, 'CustomerServiceMessage/success_message.html')

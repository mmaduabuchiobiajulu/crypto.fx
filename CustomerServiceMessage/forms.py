from django import forms
from .models import CustomerServiceMessage

class CustomerServiceMessageForm(forms.ModelForm):
    class Meta:
        model = CustomerServiceMessage
        fields = ['subject', 'message']

from django import forms
from .models import LoanApplication

class LoanApplicationForm(forms.ModelForm):
    class Meta:
        model = LoanApplication
        fields = ['full_name', 'email', 'amount', 'duration', 'purpose']
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Loan Amount'}),
            'duration': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Duration (4%/month)'}),
            # Assuming 'purpose' is a CharField, adjust as necessary for your field type
            'purpose': forms.TextInput(attrs={'class': 'form-control purpose-class', 'placeholder': 'Purpose of Loan'}),
        }
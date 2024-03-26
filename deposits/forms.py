from django import forms
from .models import CryptoDeposit, EthereumDeposit, UsdcoinDeposit, TethertDeposit

class CryptoDepositForm(forms.ModelForm):
    class Meta:
        model = CryptoDeposit
        fields = ['username', 'amount']


class EthereumDepositForm(forms.ModelForm):
    class Meta:
        model = EthereumDeposit
        fields = ['username', 'amount']


class UsdcoinDepositForm(forms.ModelForm):
    class Meta:
        model = CryptoDeposit
        fields = ['username', 'amount']


class TethertDepositForm(forms.ModelForm):
    class Meta:
        model = EthereumDeposit
        fields = ['username', 'amount']

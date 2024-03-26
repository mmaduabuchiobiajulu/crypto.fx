from django.db import models
from django.contrib.auth.models import User

class MainBalance(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='main_balance')
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.user.username}'s Main Balance"

class LoanBalance(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='loan_balance')
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.user.username}'s Loan Balance"

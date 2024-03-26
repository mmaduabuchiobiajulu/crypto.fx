from django.db import models

class LoanApplication(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.IntegerField(help_text="")
    purpose = models.CharField(max_length=255, help_text="Purpose of the loan")

    def __str__(self):
        return f"{self.full_name} - {self.amount}"





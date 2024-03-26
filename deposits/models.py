from django.db import models

# Create your models here.


class CryptoDeposit(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    username = models.CharField(max_length=10)
    amount = models.DecimalField(max_digits=19, decimal_places=10)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.username} {self.amount} by {self.user.username}"

class Transaction(models.Model):
    # other fields as before
    details = models.CharField(max_length=255, blank=True)

    # rest of your model





class EthereumDeposit(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    username = models.CharField(max_length=10)
    amount = models.DecimalField(max_digits=19, decimal_places=10)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.username} {self.amount} by {self.user.username}"

class Transaction(models.Model):
    # other fields as before
    details = models.CharField(max_length=255, blank=True)

    # rest of your model





class UsdcoinDeposit(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    username = models.CharField(max_length=10)
    amount = models.DecimalField(max_digits=19, decimal_places=10)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.username} {self.amount} by {self.user.username}"

class Transaction(models.Model):
    # other fields as before
    details = models.CharField(max_length=255, blank=True)

    # rest of your model






class TethertDeposit(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    username = models.CharField(max_length=10)
    amount = models.DecimalField(max_digits=19, decimal_places=10)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.username} {self.amount} by {self.user.username}"

class Transaction(models.Model):
    # other fields as before
    details = models.CharField(max_length=255, blank=True)

    # rest of your model

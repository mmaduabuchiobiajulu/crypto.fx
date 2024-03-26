from django.contrib import admin

from .models import CryptoDeposit, EthereumDeposit, UsdcoinDeposit, TethertDeposit

admin.site.register(CryptoDeposit)
admin.site.register(EthereumDeposit)
admin.site.register(UsdcoinDeposit)
admin.site.register(TethertDeposit)

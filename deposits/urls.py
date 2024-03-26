from django.urls import path
from .views import deposit_crypto, deposit_success, choose, bitcoin, chooseethereum, successethereum, ethereum, deposit_form_ethereum, deposit_form_usdcoin, successusdcoin, chooseusdcoin, usdcoin, deposit_form_tethert, tethert, choosetethert, successtethert

urlpatterns = [
    path('deposit/', deposit_crypto, name='deposit_crypto'),
    path('success/', deposit_success, name='success_page'),
    path('choose/', choose, name='choose'),
    path('bitcoin/', bitcoin, name='bitcoin'),

    path('deposit_form_ethereum/', deposit_form_ethereum, name='deposit_form_ethereum'),
    path('successethereum/', successethereum, name='successethereum'),
    path('chooseethereum/', chooseethereum, name='chooseethereum'),
    path('ethereum/', ethereum, name='ethereum'),
    # This line adds the success page URL

    path('deposit_form_usdcoin/', deposit_form_usdcoin, name='deposit_form_usdcoin'),
    path('successusdccoin/', successusdcoin, name='successusdcoin'),
    path('chooseusdcoin/', chooseusdcoin, name='chooseusdcoin'),
    path('usdcoin/', usdcoin, name='usdcoin'),

    path('deposit_form_tethert/', deposit_form_tethert, name='deposit_form_tethert'),
    path('successtethert/', successtethert, name='successtethert'),
    path('choosetethert/', choosetethert, name='choosetethert'),
    path('tethert/', tethert, name='tethert'),
]

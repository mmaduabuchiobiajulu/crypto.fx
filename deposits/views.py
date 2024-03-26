from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import CryptoDepositForm, EthereumDepositForm, TethertDepositForm, UsdcoinDepositForm

@login_required
def deposit_crypto(request):
    if request.method == "POST":
        form = CryptoDepositForm(request.POST)
        if form.is_valid():
            deposit = form.save(commit=False)
            deposit.user = request.user
            deposit.save()
            # Redirect to a new URL:
            return redirect('bitcoin')  # Assume 'success_page' is the name of your target URL
    else:
        form = CryptoDepositForm()
    return render(request, 'deposits/deposit_form.html', {'form': form})

def deposit_success(request):
    return render(request, 'depositsethereum/successethereum.html')


def choose(request):
    return render(request, 'deposits/choose.html')

def bitcoin(request):
    return render(request, 'deposits/bitcoin.html')






@login_required
def deposit_form_ethereum(request):
    if request.method == "POST":
        form = EthereumDepositForm(request.POST)
        if form.is_valid():
            deposit = form.save(commit=False)
            deposit.user = request.user
            deposit.save()
            # Redirect to a new URL:
            return redirect('ethereum')  # Assume 'success_page' is the name of your target URL
    else:
        form = CryptoDepositForm()
    return render(request, 'depositsethereum/deposit_form_ethereum.html', {'form': form})

def successethereum(request):
    return render(request, 'depositsethereum/successethereum.html')


def chooseethereum(request):
    return render(request, 'depositsethereum/chooseethereum.html')

def ethereum(request):
    return render(request, 'depositsethereum/ethereum.html')






@login_required
def deposit_form_usdcoin(request):
    if request.method == "POST":
        form = UsdcoinDepositForm(request.POST)
        if form.is_valid():
            deposit = form.save(commit=False)
            deposit.user = request.user
            deposit.save()
            # Redirect to a new URL:
            return redirect('usdcoin')  # Assume 'success_page' is the name of your target URL
    else:
        form = UsdcoinDepositForm()
    return render(request, 'depositsusdcoin/deposit_form_usdcoin.html', {'form': form})

def successusdcoin(request):
    return render(request, 'depositsusdcoin/successusdcoin.html')


def chooseusdcoin(request):
    return render(request, 'depositsusdcoin/chooseusdcoin.html')

def usdcoin(request):
    return render(request, 'depositsusdcoin/usdcoin.html')






@login_required
def deposit_form_tethert(request):
    if request.method == "POST":
        form = TethertDepositForm(request.POST)
        if form.is_valid():
            deposit = form.save(commit=False)
            deposit.user = request.user
            deposit.save()
            # Redirect to a new URL:
            return redirect('tethert')  # Assume 'success_page' is the name of your target URL
    else:
        form = TethertDepositForm()
    return render(request, 'depositstethert/deposit_form_tethert.html', {'form': form})

def successtethert(request):
    return render(request, 'depositstethert/successtethert.html')


def choosetethert(request):
    return render(request, 'depositstethert/choosetethert.html')

def tethert(request):
    return render(request, 'depositstethert/tethert.html')




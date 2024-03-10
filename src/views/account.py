from django.shortcuts import render, redirect
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..models import Account
from ..serializers import AccountSerializer
from ..forms import AccountForm
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.cache import cache_page

@cache_page(60 * 15)
@csrf_protect
def account_list(request):
    accounts = Account.objects.all()
    return render(request, 'account_list.html', {'accounts': accounts})


def create_account(request):
    if request.method == 'POST':
        form = AccountForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('src:account_list')  # Redirect to a success page or another URL
    else:
        form = AccountForm()
    return render(request, 'create_account.html', {'form': form})

from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.cache import cache_page
from ..models import Account
from ..forms import AccountForm
from ..decorators import only_authenticated_user


@cache_page(60 * 15)
@only_authenticated_user
def account_list(request):
    accounts = Account.objects.all()
    return render(request, 'account_list.html', {'accounts': accounts})


@only_authenticated_user
def create_account(request):
    if request.method == 'POST':
        form = AccountForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('src:account_list')  # Redirect to a success page or another URL
    else:
        form = AccountForm()
    return render(request, 'create_account.html', {'form': form})

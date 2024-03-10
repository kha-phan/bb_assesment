from django.shortcuts import render

from ..decorators import only_authenticated_user


@only_authenticated_user
def dashboard(request):
    return render(request, 'dashboard.html')

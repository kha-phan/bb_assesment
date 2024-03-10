from django.shortcuts import redirect
from functools import wraps


def redirect_authenticated_user(view, redirect_to='src:dashboard'):
    @wraps(view)
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(redirect_to)
        else:
            return view(request, *args, **kwargs)
    return wrapper


def only_authenticated_user(view, redirect_to='admin'):
    @wraps(view)
    def wrapper(request, *args, **kwargs):
        if request.user.is_anonymous:
            return redirect(redirect_to)
        else:
            return view(request, *args, **kwargs)
    return wrapper

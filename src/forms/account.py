from django import forms
from ..models import Account


class AccountForm(forms.ModelForm):
    password = forms.CharField(
        required=True,
        strip=False,
        widget=forms.PasswordInput(render_value=True, attrs={
            'id': 'login-password',
        }),
    )

    class Meta:
        model = Account
        fields = ['username', 'email', 'password']

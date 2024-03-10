from django import forms
from ..models import SupportTicketReply


class SupportTicketReplyForm(forms.ModelForm):

    class Meta:
        model = SupportTicketReply
        fields = ['message']

    widgets = {
        'message': forms.Textarea(
            attrs={
                'cols': 30,
                'rows': 3,
                'class': 'custom-areabox',
            }
        ),
    }
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.contrib import messages
from ..models.support_ticket_reply import SupportTicketReply
from ..models.account import Account
from ..models.support_ticket import SupportTicket
from ..forms import SupportTicketReplyForm


def replied_ticket_list(request):
    replies = SupportTicketReply.objects.filter(account_id=request.user.id)
    return render(request, 'replied_ticket_list.html', {'replies': replies})


def delete_reply(request, reply_id):
    reply_ticket = get_object_or_404(SupportTicketReply, id=reply_id)
    if request.method == 'POST':
        reply_ticket.delete()
        messages.success(request, 'Reply ticket deleted successfully.')
    return replied_ticket_list(request)


def create_reply_to_ticket(request, ticket_id):
    if request.method == 'POST':
        form = SupportTicketReplyForm(request.POST)
        if form.is_valid():
            replied_ticket = form.save(commit=False)
            replied_ticket.account = Account.objects.get(id=request.user.id)
            replied_ticket.support_ticket = SupportTicket.objects.get(id=ticket_id)
            replied_ticket.save()
            return redirect('src:replied_ticket_list')  # Redirect to a success page or another URL
    else:
        form = SupportTicketReplyForm()
    return render(request, 'reply_to_ticket.html', {'form': form})

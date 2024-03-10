from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.contrib import messages
from ..models.support_ticket_reply import SupportTicketReply
from ..models.account import Account
from ..models.support_ticket import SupportTicket
from ..forms import SupportTicketReplyForm
from ..decorators import only_authenticated_user


@only_authenticated_user
def replied_ticket_list(request):
    replies = SupportTicketReply.objects.all()
    return render(request, 'replied_ticket_list.html', {'replies': replies})


@only_authenticated_user
def delete_reply(request, reply_id):
    if not request.user.is_authenticated:
        return JsonResponse({'error': 'Authentication required'}, status=401)
    reply_ticket = get_object_or_404(SupportTicketReply, id=reply_id)
    # Check if the user is the owner of the reply
    if reply_ticket.account != request.user:
        return JsonResponse({'error': 'You do not have permission to delete this reply'}, status=403)
    if request.method == 'POST':
        reply_ticket.delete()
        messages.success(request, 'Reply ticket deleted successfully.')
    return replied_ticket_list(request)


@only_authenticated_user
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

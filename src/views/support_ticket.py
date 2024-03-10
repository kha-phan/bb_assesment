from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from ..models import SupportTicket, Account
from ..forms import SupportTicketForm


def ticket_on_page(request):
    ticket_list = SupportTicket.objects.all()
    paginator = Paginator(ticket_list, 10)  # Show 10 tickets per page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return page_obj


def ticket_list(request):
    tickets = SupportTicket.objects.all()
    page_obj = ticket_on_page(request)
    return render(request, 'support_ticket_list.html', {'tickets': tickets, 'page_obj': page_obj})


def create_ticket(request):
    if request.method == 'POST':
        form = SupportTicketForm(request.POST)
        if form.is_valid():
            support_ticket = form.save(commit=False)
            support_ticket.account = Account.objects.get(id=request.user.id)
            support_ticket.save()
            return redirect('src:ticket_list')
    else:
        form = SupportTicketForm()
    return render(request, 'create_ticket.html', {'form': form})

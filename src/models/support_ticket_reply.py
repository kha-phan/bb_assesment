from django.db import models
from django.utils import timezone
from .base import BaseModel
from .account import Account
from .support_ticket import SupportTicket


class SupportTicketReply(BaseModel):
    support_ticket = models.ForeignKey(SupportTicket, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Reply by {self.user.username} on {self.support_ticket.title}"

    class Meta:
        db_table = 'support_ticket_reply'

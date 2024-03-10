from django.db import models
from .base import BaseModel
from .account import Account


class SupportTicket(BaseModel):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'support_ticket'

from rest_framework import serializers
from ..models import SupportTicketReply


class SupportTicketReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = SupportTicketReply
        fields = ['id', 'ticket.js', 'user', 'message', 'created_at']

from rest_framework import serializers

from ..models import SupportTicket


class SupportTicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = SupportTicket
        fields = ['id', 'user', 'title', 'description', 'created_at']

    def validate_title(self, value):
        if not value:
            raise serializers.ValidationError("Title cannot be empty")
        return value

    def validate_description(self, value):
        if len(value) < 10:
            raise serializers.ValidationError("Description must be at least 10 characters long")
        return value

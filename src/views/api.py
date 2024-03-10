from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from ..models import SupportTicket, SupportTicketReply
from ..serializers import SupportTicketSerializer, SupportTicketReplySerializer, IsOwnerOrReadOnly


class ReplyDeleteAPIView(generics.DestroyAPIView):
    queryset = SupportTicketReply.objects.all()
    serializer_class = SupportTicketReplySerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]


class SupportTicketThreadListAPIView(generics.ListAPIView):
    queryset = SupportTicket.objects.all()
    serializer_class = SupportTicketSerializer
    pagination_class = PageNumberPagination

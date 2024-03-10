from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..models.support_ticket_reply import SupportTicketReply

@api_view(['DELETE'])
def delete_reply(request, reply_id):
    try:
        reply = SupportTicketReply.objects.get(id=reply_id)
    except SupportTicketReply.DoesNotExist:
        return Response({"error": "Reply does not exist"}, status=status.HTTP_404_NOT_FOUND)

    # Check if the user is the owner of the reply
    if reply.user != request.user:
        return Response({"error": "You are not authorized to delete this reply"}, status=status.HTTP_403_FORBIDDEN)

    # Delete the reply
    reply.delete()
    return Response({"message": "Reply deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

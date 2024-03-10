from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import dashboard, create_account, account_list, create_ticket, ticket_list, replied_ticket_list, delete_reply, create_reply_to_ticket
app_name = 'src'

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('accounts/', account_list, name='account_list'),
    path('create-account/', create_account, name='create_account'),
    path('support-tickets/', ticket_list, name='ticket_list'),
    path('create-support-tickets/', create_ticket, name='create_ticket'),
    path('replied-support-tickets/', replied_ticket_list, name='replied_ticket_list'),
    path('replied-support-tickets/<int:reply_id>/', delete_reply, name='delete_reply'),
    path('create-reply-to-ticket/<int:ticket_id>/', create_reply_to_ticket, name='create_reply_to_ticket'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)

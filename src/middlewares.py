# from .models import Account
#
#
# class VendorMiddleware:
#
#     def __init__(self, get_response):
#         self.get_response = get_response
#
#     def __call__(self, request):
#         available_clients = []
#
#         if request.user.is_authenticated:
#             if request.user.is_superuser:
#                 available_clients = Account.objects.all()
#             elif request.user.profile:
#                 available_clients = request.user.profile.clients.all()
#
#             # remove deleted vendor
#             if (request.session.get('client_id') and request.session['client_id'] not in [client.id for client in
#                                                                                           available_clients]):
#                 request.session.pop('client_id')
#                 request.session.pop('client_name')
#
#             if not request.session.get('client_id') and len(available_clients) > 0:
#                 request.session['client_id'] = available_clients[0].id
#                 request.session['client_name'] = available_clients[0].name
#
#         request.available_clients = available_clients
#         return self.get_response(request)

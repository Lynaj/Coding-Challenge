from rest_framework import routers
from backend.apps.users.views import *
from backend.apps.transactions.views import *
from backend.apps.clients.views import *

# Settings
api = routers.DefaultRouter()
api.trailing_slash = '/?'

# Users API
api.register(r'users', UserViewSet, base_name="Users Types View")

api.register(r'transactions', TransactionsViewSet, base_name="Transaction ViewSet")
api.register(r'balances', ClientBalanceViewSet, base_name="Client Balance ViewSet")

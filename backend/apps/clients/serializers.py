from rest_framework import serializers

from django.conf import settings

from generic_relations.relations import GenericRelatedField

from datetime import date

from backend.apps.clients.models import *
from backend.apps.misc.logger import *

logger = logging.getLogger(__name__)
logger.addHandler(handler)

class ClientBalanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientBalance
        fields = [
            '__all__'
        ]
from rest_framework import serializers

from django.conf import settings

from generic_relations.relations import GenericRelatedField

from datetime import date

from backend.apps.transactions.models import *
from apps.misc.logger import *

logger = logging.getLogger(__name__)
logger.addHandler(handler)

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = [
            '__all__'
        ]



from rest_framework import serializers

from django.conf import settings

from generic_relations.relations import GenericRelatedField

from datetime import date

from apps.clients.models import *
from apps.misc.logger import *

logger = logging.getLogger(__name__)
logger.addHandler(handler)

class ClientBalanceSerializer(serializers.ModelSerializer):
    currency = serializers.SerializerMethodField()
    value = serializers.SerializerMethodField()

    class Meta:
        model = ClientBalance
        fields = [
            'currency',
            'value'
        ]

    def get_currency(self, queriedObject):
        try:
            screeningQuestionDataObject = {
                'id': queriedObject.question.id,
                'question': queriedObject.question.question
            }
        except Exception as e:

            logger.error(
                "Something unexpected happened when in: ApplicantSerializer-get_personal: "
                + '\n'
                + str(e)
            )

            screeningQuestionDataObject = {
                'id': 0,
                'question': ''
            }

        return screeningQuestionDataObject

    def get_value(self, queriedObject):
        try:
            screeningQuestionDataObject = {
                'id': queriedObject.question.id,
                'question': queriedObject.question.question
            }
        except Exception as e:

            logger.error(
                "Something unexpected happened when in: ApplicantSerializer-get_personal: "
                + '\n'
                + str(e)
            )

            screeningQuestionDataObject = {
                'id': 0,
                'question': ''
            }

        return screeningQuestionDataObject

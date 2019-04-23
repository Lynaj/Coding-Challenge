import requests
import re
import os
import json
import random
import binascii
import PyPDF2
from uuid import uuid4
import io as BytesIO
from base64 import b64decode

from decimal import *

from django.db import models
from django.http import FileResponse, JsonResponse
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate, login
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.core.files.base import ContentFile
from django.utils.decorators import method_decorator
from django.core.files.storage import FileSystemStorage
from django.views.decorators.csrf import csrf_exempt
# import rest_framework_filters as filters

from apps.users.models import User
from apps.users.serializers import *

from rest_framework_jwt.serializers import VerifyJSONWebTokenSerializer
from rest_framework import permissions
from rest_framework import viewsets, status
from rest_framework.decorators import list_route, action
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import authentication, permissions
from rest_framework.authentication import BasicAuthentication
from rest_framework.parsers import MultiPartParser, JSONParser, FormParser
from rest_framework import filters

from apps.transactions.models import *
from apps.transactions.serializers import *

from apps.transactions.choices import TransactionStatusChoices

from apps.currencies.choices import CURRENCY_TYPE
from apps.currencies.models import Currency, CurrencyRatio

from apps.clients.models import Client, ClientBalance
from apps.misc.logger import *

from django.db.models import Q

logger = logging.getLogger(__name__)
logger.addHandler(handler)


class TransactionsViewSet(viewsets.ModelViewSet):
    serializer_class = TransactionSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    parser_classes = (JSONParser,)

    '''
        * @author name Arthur Drozdzyk <arturdrozdzyk@gmail.com>
        * @description 
            Returns Client object linked to the
            user, that is currently logged in 
        * @param -
        * @return - queryset
    '''
    def get_user_authenticated(self):
        queriedClient = get_object_or_404(
            Client.objects.all(),
            userObject=self.request.user
        )

        return queriedClient
    '''
        * @author name Arthur Drozdzyk <arturdrozdzyk@gmail.com>
        * @description
         Generates list of transactios processed by the currently logged user
        * @param -
        * @return - queryset
    '''
    def get_queryset(self):

        if self.request.user.is_authenticated:

            queriedClient = self.get_user_authenticated()

            queryset = Transaction.objects.filter(
                Q(
                    recipient=queriedClient
                )
                |
                Q(
                    sender=queriedClient
                )
            )

        else:
            queryset = Transaction.objects.none()

        return queryset

    '''
          * @author name Arthur Drozdzyk <arturdrozdzyk@gmail.com>
          * @description
               
               Functions responsible for transfering money, 
               as well as for converting them.
               There is no need of creating another endpoint - this one is able to handle
               both of these operations
          * @param -
          * @return -
      '''

    @list_route(methods=['POST'])
    def transfer(self, request):

        try:

            fromCurrency = request.data.get('fromCurrency', None)
            toCurrency = request.data.get('toCurrency', None)

            # Formatted as an e-mail address
            toUser= request.data.get('toUser', None)
            transactionValue = request.data.get('transactionValue', None)

            fromUser =  self.get_user_authenticated()

            # Generating list of currencies ( their abbreviations )
            listOfAcceptableCurrencies = [x[1] for x in CURRENCY_TYPE]

            # Validating input
            if (
                fromCurrency in listOfAcceptableCurrencies
                and
                toCurrency in listOfAcceptableCurrencies
                and re.match(
                    r"^[^@]+@[^@]+\.[^@]+$",
                    toUser
                )
                and
                re.match(
                    r"^\d\d*[.]?\d*$", str(transactionValue)
                )
            ):
                transactionValue = Decimal(
                    round(
                        transactionValue
                        ,
                        2
                    )
                )
                # Querying proper currency objects
                fromCurrency = get_object_or_404(
                    Currency.objects.all(),
                    abbreviation=fromCurrency
                )

                toCurrency=get_object_or_404(
                    Currency.objects.all(),
                    abbreviation=toCurrency
                )

                # Querying to user
                toUser = get_object_or_404(
                    Client.objects.all(),
                    userObject=get_object_or_404(
                        User.objects.all(),
                        email=toUser
                    )
                )

                '''
                Quering balance denoted in the currency
                delivered by the user
                '''

                # fromCurrencyFrnated = list(filter(lambda x: x[1] == fromCurrency, CURRENCY_TYPE))[0]

                # queriedCurrency = get_object_or_404(
                #     Currency.objects.all(),
                    # abbreviation=fromCurrency
                # )

                queriedSenderBalance = ClientBalance.objects.filter(
                    balanceOwner=fromUser,
                    balanceCurrency=fromCurrency
                )


                createdTransaction = Transaction.objects.create(
                    recipient=toUser,
                    sender=fromUser,
                    fromCurrency=fromCurrency,
                    toCurrency=toCurrency,
                    value=transactionValue,
                    exchangeRate=0.0,
                )


                # Determining, whether user has enough funds
                if(
                    queriedSenderBalance[0].balanceValue < transactionValue
                    or transactionValue <= 0
                ):


                    '''
                    Creating transaction object without moving any funds
                    We need this one in order to store
                    the entire history of transactions
                    even these, which could not be realized
                    '''

                    # updating transaction status
                    createdTransaction.transactionStatusChoices = list(filter(lambda x: x[1] == "Failed", TransactionStatusChoices))
                    createdTransaction.save()

                    return Response(
                        status=status.HTTP_409_CONFLICT
                    )

                else:
                    # Updating sender's balance
                    queriedSenderBalance.update(
                        balanceValue = (
                            Decimal(
                                transactionValue
                            )- queriedSenderBalance[0].balanceValue
                        )
                    )
                    # queriedSenderBalance[0].save()

                    # Updating recipient's balance
                    queriedRecipientBalance = ClientBalance.objects.filter(
                       balanceOwner=toUser,
                       balanceCurrency=toCurrency
                    )



                    '''
                    making sure that from and to currencies 
                    are the same
                    otherwise we have to convert the value of this transaction
                    '''
                    if(fromCurrency != toCurrency):
                        transactionValue *= get_object_or_404(
                            CurrencyRatio.objects.all(),
                            fromCurrency=fromCurrency,
                            toCurrency=toCurrency
                        ).ratio

                    # updating transaction status
                    createdTransaction.transactionStatusChoices = list(
                        filter(lambda x: x[1] == "Processed", TransactionStatusChoices)
                    )
                    createdTransaction.save()

                    queriedRecipientBalance.update(
                        balanceValue=(
                            Decimal(
                                transactionValue
                            ) + queriedRecipientBalance[0].balanceValue
                        )
                    )

                    return Response(
                        status=status.HTTP_200_OK
                    )

        except Exception as e:
            logger.error(
                "Something unexpected happened when in: TransactionsViewSet-transfer:"
                + '\n'
                + str(e)
            )

        return Response(
            status=status.HTTP_404_NOT_FOUND
        )

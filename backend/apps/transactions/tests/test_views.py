import json
from django.contrib.auth.models import User
from django.urls import reverse

from rest_framework import viewsets, status
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient
from rest_framework.test import APITestCase
from decimal import *

import json
import os
import codecs

getcontext().prec = 2

from apps.currencies.models import *
from apps.users.models import *
from apps.transactions.models import *
from apps.clients.models import *

from apps.currencies.choices import CURRENCY_TYPE

from misc.logger import *

logger = logging.getLogger(__name__)
logger.addHandler(handler)


class CompanyViewSetTestCase(APITestCase):
    url = reverse('api:transactions-transfer')

    # Internal Func
    def __checkTransaction(self,
                           queriedSenderBalance,
                           queriedRecipientBalance,
                           test_ratio,
                           transferValue,
                           statusOfTheTransaction,
                           isSendAndRecipientTheSame=False):
        # Making sure that the transfer took a place
        # Validating the creation of Transaction object
        queriedTransaction = Transaction.objects.all()

        self.assertEqual(
            queriedTransaction.count(),
            1
        )

        # Making sure that it's not the same user
        if (queriedSenderBalance[0].id != queriedRecipientBalance[0].id
        and isSendAndRecipientTheSame == False):
            self.assertEqual(
                queriedTransaction[0].recipient,
                self.test_second_user_client_object[0]
            )
            self.assertEqual(
                queriedTransaction[0].sender,
                self.test_first_user_client_object[0]
            )

        '''
            Making sure that
            it's not the same currency
        '''
        if (
            queriedTransaction[0].fromCurrency.abbreviation
            != queriedTransaction[0].toCurrency.abbreviation):
            self.assertEqual(
                queriedTransaction[0].fromCurrency.abbreviation,
                self.queriedCurrencies[0].abbreviation
            )
            self.assertEqual(
                queriedTransaction[0].toCurrency.abbreviation,
                self.queriedCurrencies[1].abbreviation
            )
        self.assertEqual(
            queriedTransaction[0].value,
            transferValue
        )
        self.assertEqual(
            round(
                float(queriedTransaction[0].exchangeRate),
                2
            ),
            round(
                float(test_ratio),
                2
            )
        )
        self.assertEqual(
            queriedTransaction[0].transactionStatusChoices,
            statusOfTheTransaction
        )

    def setUp(self):
        '''
            Creating default currencies
            Due to the existence of Trigger locked on Client object,
            this operation has to be completed before
            the creation of the user
        '''

        currencyIterator = iter(CURRENCY_TYPE)
        for currencies in range(len(CURRENCY_TYPE)):
            nextCurrency = next(currencyIterator)
            if (currencies == 0):
                Currency.objects.create(
                    name=nextCurrency[0],
                    abbreviation=nextCurrency[1],
                    defaultSystemCurrency=True
                )
            else:
                Currency.objects.create(
                    name=nextCurrency[0],
                    abbreviation=nextCurrency[1]
                )

        self.queriedCurrencies = Currency.objects.all()

        '''
            Making sure that number of created currencies
            matches these stored in choices.py
            '''
        self.assertEqual(
            self.queriedCurrencies.count(),
            len(CURRENCY_TYPE)
        )

        '''
        Creating & setting up test users
        as well as logging in & receiving a JWT token
        '''
        test_first_name__first_user = "Karl"
        test_last_name__first_user = "Mark"

        test_first_name__second_user = "Dmovsky"
        test_last_name__second_user = "Peter"

        test_email__first_user = "johnymarge1@wp.pl"
        test_email__second_user = "johnymar123ge1@wp.pl"

        test_password__first_user = "ij43i$#@"
        test_password__second_user = "ij43i$#@"

        url = reverse('api-jwt-auth')

        self.test_first_user = User.objects.create_user(
            first_name=test_first_name__first_user,
            last_name=test_last_name__first_user,
            email=test_email__first_user,
            password=test_password__first_user
        )

        self.test_second_user = User.objects.create_user(
            first_name=test_first_name__second_user,
            last_name=test_last_name__second_user,
            email=test_email__second_user,
            password=test_password__second_user
        )

        self.test_second_user.is_active = True
        self.test_second_user.save()

        self.test_first_user.is_active = False
        self.test_first_user.save()

        resp = self.client.post(url, {'email': test_email__first_user, 'password': test_password__first_user},
                                format='json')
        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)

        self.test_first_user.is_active = True
        self.test_first_user.save()

        self.token = ''

        resp = self.client.post(url, {'email': test_email__first_user, 'password': test_password__first_user},
                                format='json')

        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertTrue('token' in resp.data)
        self.token = resp.data['token']

        # Validating that Client object has been created & linked to the User obj
        self.test_first_user_client_object = Client.objects.filter(
            userObject=self.test_first_user
        )

        self.test_second_user_client_object = Client.objects.filter(
            userObject=self.test_second_user
        )

        self.assertEqual(self.test_first_user_client_object.count(), 1)
        self.assertEqual(self.test_second_user_client_object.count(), 1)

        verification_url = reverse('api-jwt-verify')
        resp = self.client.post(verification_url, {'token': self.token}, format='json')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)

        resp = self.client.post(verification_url, {'token': 'abc'}, format='json')
        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)

        self.client = APIClient()

    def test_fully_working_transfer__different_currencies_different_users(self):
        transferValue = 1000.0
        test_ratio = 1.1
        statusOfTheTransaction = "[('Processed', 'Processed')]"

        # Making sure user has enough funds
        queriedSenderBalance = ClientBalance.objects.filter(
            balanceOwner=self.test_first_user_client_object[0],
            balanceCurrency=self.queriedCurrencies[0]
        )

        queriedRecipientBalance = ClientBalance.objects.filter(
            balanceOwner=self.test_second_user_client_object[0],
            balanceCurrency=self.queriedCurrencies[1]
        )

        queriedSenderBalance.update(
            balanceValue=transferValue
        )

        # Making sure that the balance of the second user exists & equals 0
        self.assertEqual(
            queriedRecipientBalance.count(),
            1
        )
        self.assertEqual(
            queriedRecipientBalance[0].balanceValue,
            0.0
        )

        '''
            Creating base ratio relation
            In order to enable the algorithm
            to convert currencies
        '''
        CurrencyRatio.objects.create(
            fromCurrency=self.queriedCurrencies[0],
            toCurrency=self.queriedCurrencies[1],
            ratio=test_ratio
        )

        # Creating a request
        test_payload = {
            "fromCurrency": self.queriedCurrencies[0].abbreviation,
            "toCurrency": self.queriedCurrencies[1].abbreviation,
            "toUser": self.test_second_user.email,
            "transactionValue": transferValue
        }

        response = self.client.post(
            self.url,
            data=test_payload,
            format='json',
            HTTP_AUTHORIZATION='Bearer {}'.format(self.token)
        )

        self.assertEqual(response.status_code, 200)

        # Refreshing querysets
        queriedSenderBalance[0].refresh_from_db()
        queriedRecipientBalance[0].refresh_from_db()

        # Making sure that the transfer took a place
        self.assertEqual(
            queriedSenderBalance[0].balanceValue,
            0.0
        )

        self.assertEqual(
            queriedRecipientBalance[0].balanceValue,
            test_ratio * transferValue
        )

        # Validating the creation of Transaction object
        self.__checkTransaction(queriedSenderBalance, queriedRecipientBalance, test_ratio, transferValue,
                                statusOfTheTransaction)

    def test_fully_working_transfer__different_currencies_same_user(self):
        transferValue = 1000.0
        test_ratio = 1.1
        statusOfTheTransaction = "[('Processed', 'Processed')]"

        # Making sure user has enough funds
        queriedSenderBalance = ClientBalance.objects.filter(
            balanceOwner=self.test_first_user_client_object[0],
            balanceCurrency=self.queriedCurrencies[0]
        )

        queriedRecipientBalance = ClientBalance.objects.filter(
            balanceOwner=self.test_first_user_client_object[0],
            balanceCurrency=self.queriedCurrencies[1]
        )

        queriedSenderBalance.update(
            balanceValue=transferValue
        )

        # Making sure that the balance of the second user exists & equals 0
        self.assertEqual(
            queriedRecipientBalance.count(),
            1
        )
        self.assertEqual(
            queriedRecipientBalance[0].balanceValue,
            0.0
        )

        '''
            Creating base ratio relation
            In order to enable the algorithm
            to convert currencies
        '''
        CurrencyRatio.objects.create(
            fromCurrency=self.queriedCurrencies[0],
            toCurrency=self.queriedCurrencies[1],
            ratio=test_ratio
        )

        # Creating a request
        test_payload = {
            "fromCurrency": self.queriedCurrencies[0].abbreviation,
            "toCurrency": self.queriedCurrencies[1].abbreviation,
            "toUser": self.test_first_user.email,
            "transactionValue": transferValue
        }

        response = self.client.post(
            self.url,
            data=test_payload,
            format='json',
            HTTP_AUTHORIZATION='Bearer {}'.format(self.token)
        )

        self.assertEqual(response.status_code, 200)

        # Refreshing querysets
        queriedSenderBalance[0].refresh_from_db()
        queriedRecipientBalance[0].refresh_from_db()

        # Making sure that the transfer took a place
        self.assertEqual(
            queriedSenderBalance[0].balanceValue,
            0.0
        )

        self.assertEqual(
            queriedRecipientBalance[0].balanceValue,
            test_ratio * transferValue
        )

        # Validating the creation of Transaction object
        self.__checkTransaction(queriedSenderBalance, queriedRecipientBalance, test_ratio, transferValue,
                                statusOfTheTransaction, True)

    def test_fully_working_transfer__same_currencies_same_user(self):
        transferValue = 1000.0
        test_ratio = 1.1
        statusOfTheTransaction = "[('Processed', 'Processed')]"

        # Making sure user has enough funds
        queriedSenderBalance = ClientBalance.objects.filter(
            balanceOwner=self.test_first_user_client_object[0],
            balanceCurrency=self.queriedCurrencies[0]
        )

        queriedRecipientBalance = ClientBalance.objects.filter(
            balanceOwner=self.test_first_user_client_object[0],
            balanceCurrency=self.queriedCurrencies[0]
        )

        queriedSenderBalance.update(
            balanceValue=transferValue
        )

        # Making sure that the balance of the second user exists & equals 0
        self.assertEqual(
            queriedRecipientBalance.count(),
            1
        )
        self.assertEqual(
            queriedRecipientBalance[0].balanceValue,
            transferValue
        )

        '''
            Creating base ratio relation
            In order to enable the algorithm
            to convert currencies
        '''
        CurrencyRatio.objects.create(
            fromCurrency=self.queriedCurrencies[0],
            toCurrency=self.queriedCurrencies[0],
            ratio=test_ratio
        )

        # Creating a request
        test_payload = {
            "fromCurrency": self.queriedCurrencies[0].abbreviation,
            "toCurrency": self.queriedCurrencies[0].abbreviation,
            "toUser": self.test_first_user.email,
            "transactionValue": transferValue
        }

        response = self.client.post(
            self.url,
            data=test_payload,
            format='json',
            HTTP_AUTHORIZATION='Bearer {}'.format(self.token)
        )

        self.assertEqual(response.status_code, 200)

        # Refreshing querysets
        queriedSenderBalance[0].refresh_from_db()
        queriedRecipientBalance[0].refresh_from_db()

        # Making sure that the transfer took a place
        self.assertEqual(
            queriedSenderBalance[0].balanceValue,
            transferValue
        )

        self.assertEqual(
            queriedRecipientBalance[0].balanceValue,
            transferValue
        )

        # Validating the creation of Transaction object
        self.__checkTransaction(queriedSenderBalance, queriedRecipientBalance, 1.0, transferValue,
                                statusOfTheTransaction, True)

    def test_lack_of_funds_error__same_currencies_same_user(self):
        transferValue = 1000.0
        test_ratio = 1.1
        statusOfTheTransaction = "[('Failed', 'Failed')]"

        # Making sure user has enough funds
        queriedSenderBalance = ClientBalance.objects.filter(
            balanceOwner=self.test_first_user_client_object[0],
            balanceCurrency=self.queriedCurrencies[0]
        )

        queriedRecipientBalance = ClientBalance.objects.filter(
            balanceOwner=self.test_first_user_client_object[0],
            balanceCurrency=self.queriedCurrencies[0]
        )

        queriedSenderBalance.update(
            balanceValue=0.0
        )

        # Making sure that the balance of the second user exists & equals 0
        self.assertEqual(
            queriedRecipientBalance.count(),
            1
        )
        self.assertEqual(
            queriedRecipientBalance[0].balanceValue,
            0.0
        )

        '''
            Creating base ratio relation
            In order to enable the algorithm
            to convert currencies
        '''
        CurrencyRatio.objects.create(
            fromCurrency=self.queriedCurrencies[0],
            toCurrency=self.queriedCurrencies[0],
            ratio=test_ratio
        )

        # Creating a request
        test_payload = {
            "fromCurrency": self.queriedCurrencies[0].abbreviation,
            "toCurrency": self.queriedCurrencies[0].abbreviation,
            "toUser": self.test_first_user.email,
            "transactionValue": transferValue
        }

        response = self.client.post(
            self.url,
            data=test_payload,
            format='json',
            HTTP_AUTHORIZATION='Bearer {}'.format(self.token)
        )

        self.assertEqual(response.status_code, 409)

        # Refreshing querysets
        queriedSenderBalance[0].refresh_from_db()
        queriedRecipientBalance[0].refresh_from_db()

        # Making sure that the transfer took a place
        self.assertEqual(
            queriedSenderBalance[0].balanceValue,
            0.0
        )

        self.assertEqual(
            queriedRecipientBalance[0].balanceValue,
            0.0
        )

        # Validating the creation of Transaction object
        self.__checkTransaction(queriedSenderBalance, queriedRecipientBalance, 1.0, transferValue,
                                statusOfTheTransaction)

    def test_lack_of_funds_error__different_currencies_same_user(self):

        transferValue = 1000.0
        test_ratio = 1.1
        statusOfTheTransaction = "[('Failed', 'Failed')]"

        # Making sure user has enough funds
        queriedSenderBalance = ClientBalance.objects.filter(
            balanceOwner=self.test_first_user_client_object[0],
            balanceCurrency=self.queriedCurrencies[0]
        )

        queriedRecipientBalance = ClientBalance.objects.filter(
            balanceOwner=self.test_first_user_client_object[0],
            balanceCurrency=self.queriedCurrencies[1]
        )

        queriedSenderBalance.update(
            balanceValue=0.0
        )

        # Making sure that the balance of the second user exists & equals 0
        self.assertEqual(
            queriedRecipientBalance.count(),
            1
        )
        self.assertEqual(
            queriedRecipientBalance[0].balanceValue,
            0.0
        )

        '''
            Creating base ratio relation
            In order to enable the algorithm
            to convert currencies
        '''
        CurrencyRatio.objects.create(
            fromCurrency=self.queriedCurrencies[0],
            toCurrency=self.queriedCurrencies[1],
            ratio=test_ratio
        )

        # Creating a request
        test_payload = {
            "fromCurrency": self.queriedCurrencies[0].abbreviation,
            "toCurrency": self.queriedCurrencies[1].abbreviation,
            "toUser": self.test_first_user.email,
            "transactionValue": transferValue
        }

        response = self.client.post(
            self.url,
            data=test_payload,
            format='json',
            HTTP_AUTHORIZATION='Bearer {}'.format(self.token)
        )

        self.assertEqual(response.status_code, 409)

        # Refreshing querysets
        queriedSenderBalance[0].refresh_from_db()
        queriedRecipientBalance[0].refresh_from_db()

        # Making sure that the transfer took a place
        self.assertEqual(
            queriedSenderBalance[0].balanceValue,
            0.0
        )

        self.assertEqual(
            queriedRecipientBalance[0].balanceValue,
            0.0
        )

        # Validating the creation of Transaction object
        self.__checkTransaction(queriedSenderBalance, queriedRecipientBalance, test_ratio, transferValue, statusOfTheTransaction,
                                True)

    def test_lack_of_funds_error__different_currencies_different_users(self):
        transferValue = 1000.0
        test_ratio = 1.1
        statusOfTheTransaction = "[('Failed', 'Failed')]"

        # Making sure user has enough funds
        queriedSenderBalance = ClientBalance.objects.filter(
            balanceOwner=self.test_first_user_client_object[0],
            balanceCurrency=self.queriedCurrencies[0]
        )

        queriedRecipientBalance = ClientBalance.objects.filter(
            balanceOwner=self.test_second_user_client_object[0],
            balanceCurrency=self.queriedCurrencies[1]
        )

        queriedSenderBalance.update(
            balanceValue=0.0
        )

        # Making sure that the balance of the second user exists & equals 0
        self.assertEqual(
            queriedRecipientBalance.count(),
            1
        )
        self.assertEqual(
            queriedRecipientBalance[0].balanceValue,
            0.0
        )

        '''
            Creating base ratio relation
            In order to enable the algorithm
            to convert currencies
        '''
        CurrencyRatio.objects.create(
            fromCurrency=self.queriedCurrencies[0],
            toCurrency=self.queriedCurrencies[1],
            ratio=test_ratio
        )

        # Creating a request
        test_payload = {
            "fromCurrency": self.queriedCurrencies[0].abbreviation,
            "toCurrency": self.queriedCurrencies[1].abbreviation,
            "toUser": self.test_second_user.email,
            "transactionValue": transferValue
        }

        response = self.client.post(
            self.url,
            data=test_payload,
            format='json',
            HTTP_AUTHORIZATION='Bearer {}'.format(self.token)
        )

        self.assertEqual(response.status_code, 409)

        # Refreshing querysets
        queriedSenderBalance[0].refresh_from_db()
        queriedRecipientBalance[0].refresh_from_db()

        # Making sure that the transfer took a place
        self.assertEqual(
            queriedSenderBalance[0].balanceValue,
            0.0
        )

        self.assertEqual(
            queriedRecipientBalance[0].balanceValue,
            0.0
        )

        # Validating the creation of Transaction object
        self.__checkTransaction(queriedSenderBalance, queriedRecipientBalance, test_ratio, transferValue, statusOfTheTransaction)

    def test_negative_transfer_value_positive_balance_of_sender__different_currencies_different_users(self):
        transferValue = -1000.0
        balanceOfSender = 1000.0
        test_ratio = 1.1
        statusOfTheTransaction = "[('Failed', 'Failed')]"

        # Making sure user has enough funds
        queriedSenderBalance = ClientBalance.objects.filter(
            balanceOwner=self.test_first_user_client_object[0],
            balanceCurrency=self.queriedCurrencies[0]
        )

        queriedRecipientBalance = ClientBalance.objects.filter(
            balanceOwner=self.test_second_user_client_object[0],
            balanceCurrency=self.queriedCurrencies[1]
        )

        queriedSenderBalance.update(
            balanceValue=balanceOfSender
        )

        # Making sure that the balance of the second user exists & equals 0
        self.assertEqual(
            queriedRecipientBalance.count(),
            1
        )
        self.assertEqual(
            queriedRecipientBalance[0].balanceValue,
            0.0
        )

        '''
            Creating base ratio relation
            In order to enable the algorithm
            to convert currencies
        '''
        CurrencyRatio.objects.create(
            fromCurrency=self.queriedCurrencies[0],
            toCurrency=self.queriedCurrencies[1],
            ratio=test_ratio
        )

        # Creating a request
        test_payload = {
            "fromCurrency": self.queriedCurrencies[0].abbreviation,
            "toCurrency": self.queriedCurrencies[1].abbreviation,
            "toUser": self.test_second_user.email,
            "transactionValue": transferValue
        }

        response = self.client.post(
            self.url,
            data=test_payload,
            format='json',
            HTTP_AUTHORIZATION='Bearer {}'.format(self.token)
        )

        self.assertEqual(response.status_code, 404)

        # Refreshing querysets
        queriedSenderBalance[0].refresh_from_db()
        queriedRecipientBalance[0].refresh_from_db()

        # Making sure that the transfer took a place
        self.assertEqual(
            queriedSenderBalance[0].balanceValue,
            balanceOfSender
        )

        self.assertEqual(
            queriedRecipientBalance[0].balanceValue,
            0.0
        )

    def test_large_float_points_attack__different_currencies_different_users(self):
        transferValue = 0.000001
        balanceOfSender = 1000.0
        test_ratio = 1.1
        statusOfTheTransaction = "[('Failed', 'Failed')]"

        # Making sure user has enough funds
        queriedSenderBalance = ClientBalance.objects.filter(
            balanceOwner=self.test_first_user_client_object[0],
            balanceCurrency=self.queriedCurrencies[0]
        )

        queriedRecipientBalance = ClientBalance.objects.filter(
            balanceOwner=self.test_second_user_client_object[0],
            balanceCurrency=self.queriedCurrencies[1]
        )

        queriedSenderBalance.update(
            balanceValue=balanceOfSender
        )

        # Making sure that the balance of the second user exists & equals 0
        self.assertEqual(
            queriedRecipientBalance.count(),
            1
        )
        self.assertEqual(
            queriedRecipientBalance[0].balanceValue,
            0.0
        )

        '''
            Creating base ratio relation
            In order to enable the algorithm
            to convert currencies
        '''
        CurrencyRatio.objects.create(
            fromCurrency=self.queriedCurrencies[0],
            toCurrency=self.queriedCurrencies[1],
            ratio=test_ratio
        )

        # Creating a request
        test_payload = {
            "fromCurrency": self.queriedCurrencies[0].abbreviation,
            "toCurrency": self.queriedCurrencies[1].abbreviation,
            "toUser": self.test_second_user.email,
            "transactionValue": transferValue
        }

        response = self.client.post(
            self.url,
            data=test_payload,
            format='json',
            HTTP_AUTHORIZATION='Bearer {}'.format(self.token)
        )

        self.assertEqual(response.status_code, 404)

        # Refreshing querysets
        queriedSenderBalance[0].refresh_from_db()
        queriedRecipientBalance[0].refresh_from_db()

        # Making sure that the transfer took a place
        self.assertEqual(
            queriedSenderBalance[0].balanceValue,
            balanceOfSender
        )

        self.assertEqual(
            queriedRecipientBalance[0].balanceValue,
            0.0
        )

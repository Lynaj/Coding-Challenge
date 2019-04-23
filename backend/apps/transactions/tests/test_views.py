import json
from django.contrib.auth.models import User
from django.urls import reverse

from rest_framework import viewsets, status
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient
from rest_framework.test import APITestCase

import json
import os
import codecs

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

        test_email__first_user= "johnymarge1@wp.pl"
        test_email__second_user= "johnymar123ge1@wp.pl"

        test_password__first_user = "ij43i$#@"
        test_password__second_user= "ij43i$#@"

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

        resp = self.client.post(url, {'email': test_email__first_user, 'password': test_password__first_user}, format='json')
        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)

        self.test_first_user.is_active = True
        self.test_first_user.save()

        self.token = ''

        resp = self.client.post(url, {'email': test_email__first_user, 'password': test_password__first_user}, format='json')

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
            balanceValue = transferValue
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
            fromCurrency = self.queriedCurrencies[0],
            toCurrency = self.queriedCurrencies[1],
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
            test_ratio*transferValue
        )


    def TTtest_fully_working_transfer__different_currencies_same_user(self):
        raise NotImplementedError()

    def TTtest_fully_working_transfer__same_currencies_same_user(self):
        raise NotImplementedError()

    def TTtest_lack_of_funds_error__same_currencies_same_user(self):
        raise NotImplementedError()

    def TTtest_lack_of_funds_error__different_currencies_same_user(self):
        raise NotImplementedError()

    def TTtest_lack_of_funds_error__different_currencies_different_users(self):
        raise NotImplementedError()

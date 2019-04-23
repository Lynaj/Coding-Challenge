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

from backend.apps.currencies.models import *
from backend.apps.users.models import *
from backend.apps.transactions.models import *
from backend.apps.clients.models import *

from backend.apps.currencies.choices import CURRENCY_TYPE

from backend.misc.logger import *
from backend.apps.misc.authentication import *

logger = logging.getLogger(__name__)
logger.addHandler(handler)


class CompanyViewSetTestCase(APITestCase):
    url = reverse('api:offers-crt')

    def setUp(self):
        '''
            Creating default currencies
            Due to the existence of Trigger locked on Client object,
            this operation has to be completed before
            the creation of the user
        '''


        urrencyIterator = iter(CURRENCY_TYPE)
        for currencies in range(len(CURRENCY_TYPE)):
            if (currencies == 0):
                Currency.objects.create(
                    name=next(currencyIterator)[0],
                    abbreviation=next(currencyIterator)[1]
                )
            else:
                Currency.objects.create(
                    name=next(currencyIterator)[0],
                    abbreviation=next(currencyIterator)[1],
                    defaultSystemCurrency=True
                )

        self.queriedCurrencies = Currency.objects.all()

        '''
            Making sure that number of created currencies
            matches these stored in choices.py
            '''
        self.assertEqual(
            self.queriedCurrencies.count(),
            range(len(CURRENCY_TYPE))
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
        test_email__second_user= "johnymarge1@wp.pl"

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

        self.assertEqual(self.test_first_user.count(), 1)
        self.assertEqual(self.test_second_user.count(), 1)

        verification_url = reverse('api-jwt-verify')
        resp = self.client.post(verification_url, {'token': self.token}, format='json')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)

        resp = self.client.post(verification_url, {'token': 'abc'}, format='json')
        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)

        self.client = APIClient()


    def test_fully_working_transfer__different_currencies_different_users(self):
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
            balanceValue = 1000
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

        # Creating a request
        test_payload = {
            "fromCurrency": self.queriedCurrencies[0],
            "toCurrency": self.queriedCurrencies[1],
            "toUser": self.test_second_user.email,
        }

        response = self.client.post(
            self.url,
            {},
            HTTP_AUTHORIZATION='Bearer {}'.format(self.token)
        )

        self.assertEqual(response.status_code, 200)

        self.assertEqual(
            User.objects.all().count(),
            1
        )

        self.assertEqual(
            Offer.objects.all().count(),
            1
        )

        logger.error('Offer.objects.all()[0]: ' + str(Offer.objects.all()[0]))

    def test_fully_working_transfer__different_currencies_same_user(self):
        raise NotImplementedError()

    def test_fully_working_transfer__same_currencies_same_user(self):
        raise NotImplementedError()

    def test_lack_of_funds_error__same_currencies_same_user(self):
        raise NotImplementedError()

    def test_lack_of_funds_error__different_currencies_same_user(self):
        raise NotImplementedError()

    def test_lack_of_funds_error__different_currencies_different_users(self):
        raise NotImplementedError()

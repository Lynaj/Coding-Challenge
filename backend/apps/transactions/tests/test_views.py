import json
from django.contrib.auth.models import User
from django.urls import reverse

from rest_framework import viewsets, status
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient
from rest_framework.test import APITestCase

from apps.offers.models import *
from apps.offers.serializers import *

import json
import os
import codecs

from apps.misc.logger import *
from apps.misc.authentication import *

logger = logging.getLogger(__name__)
logger.addHandler(handler)


class CompanyViewSetTestCase(APITestCase):
    url = reverse('api:offers-crt')

    def setUp(self):
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


        verification_url = reverse('api-jwt-verify')
        resp = self.client.post(verification_url, {'token': self.token}, format='json')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)

        resp = self.client.post(verification_url, {'token': 'abc'}, format='json')
        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)

        self.client = APIClient()

    def test_fully_working_transfer__different_currencies_different_users(self):
        raise NotImplementedError()

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

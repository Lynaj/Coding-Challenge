
from apps.currencies.models import *
from apps.users.models import *
from apps.transactions.models import *
from apps.clients.models import *

from apps.currencies.choices import CURRENCY_TYPE

from misc.logger import *

logger = logging.getLogger(__name__)
logger.addHandler(handler)

from django.test import TestCase
from decentmark.models import *

class ClientModelTest(TestCase):
    
    def setUp(cls):
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

        test_email__first_user= "johnymarge1@wp.pl"

        test_password__first_user = "ij43i$#@"

        url = reverse('api-jwt-auth')

        testUserObject = User.objects.create_user(
            first_name=test_first_name__first_user,
            last_name=test_last_name__first_user,
            email=test_email__first_user,
            password=test_password__first_user
        )

        testnativeAccountCurrency = self.queriedCurrencies[0]

        # Creating test client object
        Client.objects.create(
            userObject=testUserObject,
            nativeAccountCurrency=testnativeAccountCurrency
        )

    def test_userObject_label(self):
        unit = Client.objects.get(id=1)
        field_label = unit._meta.get_field('userObject').verbose_name
        self.assertEquals(field_label, 'Linked user object')

    def test_nativeAccountCurrency_label(self):
        unit = Client.objects.get(id=1)
        field_label = unit._meta.get_field('nativeAccountCurrency').verbose_name
        self.assertEquals(field_label, 'Linked currency')



class ClientBalanceModelTest(TestCase):
    
    def setUp(cls):
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
        test_email__first_user= "johnymarge1@wp.pl"
        test_password__first_user = "ij43i$#@"

        url = reverse('api-jwt-auth')

        testUserObject = User.objects.create_user(
            first_name=test_first_name__first_user,
            last_name=test_last_name__first_user,
            email=test_email__first_user,
            password=test_password__first_user
        )

        testnativeAccountCurrency = self.queriedCurrencies[0]
        
        # Creating test client object
        testClient = Client.objects.create(
            userObject=testUserObject,
            nativeAccountCurrency=testnativeAccountCurrency
        )

        # Creating test ClientBalance object
        ClientBalance.objects.create(
            balanceOwner=testClient,
            balanceCurrency=self.queriedCurrencies[0],
            balanceValue=
        )

    def test_balanceOwner_label(self):
        unit = ClientBalance.objects.get(id=1)
        field_label = unit._meta.get_field('balanceOwner').verbose_name
        self.assertEquals(field_label, 'Linked ClientBalance object')

    def test_balanceCurrency_label(self):
        unit = ClientBalance.objects.get(id=1)
        field_label = unit._meta.get_field('balanceCurrency').verbose_name
        self.assertEquals(field_label, 'Linked currency')

    def test_balanceValue_label(self):
        unit = ClientBalance.objects.get(id=1)
        field_label = unit._meta.get_field('balanceValue').verbose_name
        self.assertEquals(field_label, 'Value of the balance')
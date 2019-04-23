from uuid import uuid4

from django.db.models.signals import post_save, pre_save, pre_delete, post_delete
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.utils import timezone
import uuid

from backend.apps.users.models import User
from backend.apps.currencies.models import Currency
from backend.apps.misc.logger import *

env = environ.Env()

# +++++++++++++++++++++++++++++++++++
logger = logging.getLogger(__name__)
logger.addHandler(handler)
# +++++++++++++++++++++++++++++++++++


class Client(models.Model):
    userObject = models.ForeignKey(
        User,
        null=False,
        blank=False,
        on_delete=models.CASCADE,
        verbose_name='Linked user object'
    )

    nativeAccountCurrency= models.ForeignKey(
        Currency,
        null=False,
        blank=False,
        on_delete=models.CASCADE,
        verbose_name='Linked currency'
    )

    created_at = models.DateTimeField(
        verbose_name='Created at',
        auto_now_add=timezone.now
    )

    updated_at = models.DateTimeField(
        verbose_name='Updated at',
        blank=True,
        auto_now_add=timezone.now
    )



class ClientBalance(models.Model):
    balanceOwner = models.ForeignKey(
        Client,
        null=False,
        blank=False,
        on_delete=models.CASCADE,
        verbose_name='Linked Client object'
    )

    balanceCurrency = models.ForeignKey(
        Currency,
        null=False,
        blank=False,
        on_delete=models.CASCADE,
        verbose_name='Linked currency'
    )

    balanceValue = models.DecimalField(
        default=0.0,
        max_digits=190,
        null=True,
        decimal_places=4,
        verbose_name='Value of the balance'
    )

    created_at = models.DateTimeField(
        verbose_name='Created at',
        auto_now_add=timezone.now
    )

    updated_at = models.DateTimeField(
        verbose_name='Updated at',
        blank=True,
        auto_now_add=timezone.now
    )


'''
    * @author name Arthur Drozdzyk <arturdrozdzyk@gmail.com>
    * @description 
        The method is creating ClientBalance for each and every available currency
        & linking it with corresponded Client account
    * @param -
    * @return -
'''

def CreateBasicCurrencyStack(sender,
                        instance,
                        created,
                        raw,
                        using,
                        update_fields,
                        **kwargs):
    if created:

        try:

            for currency in Currency.objects.all():
                '''
                    determining with given currency is a default
                    one or not
                    If so, it's value should equal hard-coded value
                '''
                balanceValue = 0

                if(currency.defaultSystemCurrency):
                    balanceValue = env.bool('DEFAULT_CURRENCY_VALUE')

                ClientBalance.objects.create(
                    balanceOwner=instance,
                    balanceCurrency=currency,
                    balanceValue=0
                )

        except Exception as e:
            logger.error(
                '[*** TRIGGER ***] [ ERROR ] [ CreateBasicCurrencyStack ] '
                +
                'Problem: exception occured during the process of creating ClientBalance'
                + 'error: ' + str(e)
            )

post_save.connect(CreateBasicCurrencyStack, sender=Client)
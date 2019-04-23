from uuid import uuid4

from django.db.models.signals import post_save, pre_save, pre_delete, post_delete
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.utils import timezone
import uuid

from apps.clients.models import Client
from apps.exchange.models import ExchangeRate
from apps.currencies.models import Currency, CurrencyRatio

from backend.apps.misc.logger import *
from apps.transactions.choices import TransactionStatusChoices

# +++++++++++++++++++++++++++++++++++
logger = logging.getLogger(__name__)
logger.addHandler(handler)
# +++++++++++++++++++++++++++++++++++


class Transaction(models.Model):
    recipient = models.ForeignKey(
        Client,
        null=False,
        on_delete=models.SET_NULL,
        verbose_name='Recipient of the transaction'
    )

    sender = models.ForeignKey(
        Client,
        null=False,
        on_delete=models.SET_NULL,
        verbose_name='Creator of the transaction'
    )

    currency = models.ForeignKey(
        Currency,
        null=False,
        on_delete=models.SET_NULL,
        verbose_name='Base currency of the transaction'
    )

    value = models.DecimalField(
        default=0.0,
        max_digits=190,
        null=False,
        decimal_places=4,
        verbose_name='Value of the transaction denoted in the given currency'
    )

    exchangeRate = models.DecimalField(
        default=0.0,
        max_digits=190,
        null=False,
        decimal_places=4,
        verbose_name='Ratio of currencies used in the transaction'
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

    class Meta:
        verbose_name = 'Transaction'
        verbose_name_plural = 'Transactions'

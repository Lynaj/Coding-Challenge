from uuid import uuid4

from django.db.models.signals import post_save, pre_save, pre_delete, post_delete
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.utils import timezone
import uuid

from backend.apps.misc.logger import *
from backend.apps.currencies.choices import *

# +++++++++++++++++++++++++++++++++++
logger = logging.getLogger(__name__)
logger.addHandler(handler)
# +++++++++++++++++++++++++++++++++++


class Currency(models.Model):
    name = models.CharField(
        choices=CURRENCY_TYPE,
        default=next(iter(CURRENCY_TYPE))[0],
        max_length=300,
        null=False,
        verbose_name='Name of the currency'
    )

    abbreviation = models.CharField(
        choices=CURRENCY_TYPE,
        default=next(iter(CURRENCY_TYPE))[1],
        max_length=30,
        null=False,
        verbose_name='Abbreviation of the currency'
    )

    defaultSystemCurrency = models.BooleanField(
        default=False,
        verbose_name='Is a default currency of the entire system'
    )


class CurrencyRatio(models.Model):
    fromCurrency = models.ForeignKey(
        Currency,
        null=False,
        blank=False,
        on_delete=models.CASCADE,
        verbose_name='First currency of the relation'
    )

    toCurrency = models.ForeignKey(
        Currency,
        null=False,
        blank=False,
        on_delete=models.CASCADE,
        verbose_name='Second currency of the relation'
    )

    ratio = models.DecimalField(
        default=0.0,
        max_digits=190,
        null=True,
        decimal_places=4,
        verbose_name='Ratio of linked currencies'
    )
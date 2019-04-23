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

    balanceVaue = models.DecimalField(
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

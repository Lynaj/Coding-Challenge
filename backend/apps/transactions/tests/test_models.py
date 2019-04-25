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


class UnitModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Unit.objects.create(name='Python', start='2018-10-25 14:30:59', 
                            end='2017-10-25 14:30:59', description='111',
                            deleted='False')

    def test_name_label(self):
        unit = Unit.objects.get(id=1)
        field_label = unit._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_name_max_length(self):
        unit = Unit.objects.get(id=1)
        max_length = unit._meta.get_field('name').max_length
        self.assertEquals(max_length, 200)

    def test_str(self):
        unit = Unit.objects.get(id=1)
        expected_object_name = unit.name
        self.assertEquals(expected_object_name, str(unit))

    def test_date(self):
        unit = Unit.objects.get(id=1)
        with self.assertRaises(ValidationError):
            unit.full_clean()
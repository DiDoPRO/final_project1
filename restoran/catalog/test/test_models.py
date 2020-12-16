from django.test import TestCase

# Create your tests here.

from catalog.models import Table


class TableModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        """Set up non-modified objects used by all test methods."""
        Table.objects.create( number=None)

    def test_number_label(self):
        table = Table.objects.get(id=1)
        field_label = table._meta.get_field('number').verbose_number
        self.assertEquals(field_label, 'number')

    def test_number_max_length(self):
        table = Table.objects.get(id=1)
        max_length = table._meta.get_field('number').max_length
        self.assertEquals(max_length, 100)

    def test_get_absolute_url(self):
        table = Table.objects.get(id=1)
        # This will also fail if the urlconf is not defined.
        self.assertEquals(table.get_absolute_url(), '/catalog/table/1')

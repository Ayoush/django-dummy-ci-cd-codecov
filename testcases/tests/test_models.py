from django.test import TestCase
from testcases.models import Org
from django.db.utils import IntegrityError
class TestModels(TestCase):
    def setUp(self):
        self.org1 = Org.objects.create(name='Org1', email='org1@email.com')
        self.org2 = Org.objects.create(name='Org2', email='org2@email.com')

    def test_org_slug(self):
        self.assertEquals(self.org1.slug, 'org1')
        self.assertEquals(self.org2.slug, 'org2')

    def test_org_name_uniqueness(self):
         with self.assertRaises(IntegrityError):
             Org.objects.create(name='Org1', email='org1@email.com')

    def test_org_actually_getting_created(self):
          self.assertEquals(self.org1.name, 'Org1')       
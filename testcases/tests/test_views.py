from django.test import TestCase, Client
from testcases.views import org_index
from django.urls import reverse
from testcases.models import Org

class TestViews(TestCase):
    def setUp(self):
        self.org1 = Org.objects.create(name='Org1', email='org1@email.com')
        self.org2 = Org.objects.create(name='Org2', email='org2@email.com')
        self.client = Client()
        self.response = self.client.get(reverse('org_index'))

    def test_org_index(self):
        org1 = self.response.json()[0]
        self.assertEquals(self.org1.slug, org1['slug'])
        self.assertEquals(self.response.status_code, 200)


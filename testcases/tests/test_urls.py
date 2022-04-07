from django.test import SimpleTestCase
from django.urls import reverse, resolve
from testcases.views import org_index
class TestUrls(SimpleTestCase):
    def test_org_index(self):
        url = reverse('org_index')
        self.assertEquals(resolve(url).func, org_index)
        

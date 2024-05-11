from django.test import TestCase
import sys
sys.path.append("..")
from main.models import SiteSection

class SiteSectionTest(TestCase):


    @classmethod
    def setUpTestData(cls):
        SiteSection.objects.create(id = 0, display_text = "Test Text", icon_url = "Some icon", navigation_url = "Some Path")
    
    def test_id_label(self):
        siteSection = SiteSection.objects.get(pk = 0)
        id_label = siteSection._meta.get_field('id').verbose_name
        self.assertEquals(id_label, 'id')
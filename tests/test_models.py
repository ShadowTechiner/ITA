from django.test import TestCase
from django.db.utils import IntegrityError
import sys
sys.path.append("..")
from main.models import SiteSection

class SiteSectionTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        SiteSection.objects.create(id = 0, display_text = "Data", icon_url = "Some icon", navigation_path_name = "data")
        SiteSection.objects.create(id = 1, display_text = "Similar Tickets", icon_url = "Some icon", navigation_path_name = "similartickets")
        SiteSection.objects.create(id = 2, display_text = "Modules", icon_url = "Some icon", navigation_path_name = "modules")
        SiteSection.objects.create(id = 3, display_text = "Pipelines", icon_url = "Some icon", navigation_path_name = "pipelines")
        SiteSection.objects.create(id = 4, display_text = "Test Text", icon_url = "Some icon", navigation_path_name = "SomePath")

    def check_field_label(self, field, expected_label):
        site_section = SiteSection.objects.get(pk = 0)
        field_label = site_section._meta.get_field(field).verbose_name
        self.assertEquals(field_label, expected_label)

    def check_max_length(self, field, expected_result):
        site_section = SiteSection.objects.get(pk = 0)
        max_length = site_section._meta.get_field(field).max_length
        self.assertEqual(max_length, expected_result)

    def test_id_label(self):
        self.check_field_label('id', 'ID')
    
    def test_display_text_label(self):
        self.check_field_label('display_text', 'Display Text')
    
    def test_icon_url_label(self):
        self.check_field_label('icon_url', 'Icon URL')
    
    def test_navigation_path_name_label(self):
        self.check_field_label('navigation_path_name', 'Path Name')

    def test_object_name_is_section_label_with_display_text(self):
        site_sections = SiteSection.objects.all()
        site_section_string_representations = [str(site_section) for site_section in site_sections]
        expected_results = ['Section: Data', 'Section: Similar Tickets', 'Section: Modules', 'Section: Pipelines', 'Section: Test Text']
        self.assertEqual(site_section_string_representations, expected_results)

    def test_add_record_with_existing_id_throws_IntegrityError(self):
        self.assertRaises(IntegrityError, lambda : SiteSection.objects.create(id = 0, display_text = "test", icon_url = "test", navigation_path_name = "test"))

    def test_display_text_max_length(self):
        self.check_max_length('display_text', 30)
    
    def test_icon_url_max_length(self):
        self.check_max_length('icon_url', 100)
    
    def test_navigation_path_name_max_length(self):
        self.check_max_length('navigation_path_name', 100)
    
    def test_navigation_path_name_default_value(self):
        site_section = SiteSection.objects.get(pk = 0)
        default_value = site_section._meta.get_field('navigation_path_name').default
        self.assertEqual(default_value, '#')
    
    def test_get_navigation_url(self):
        site_sections = SiteSection.objects.all()
        urls = [site_section.get_navigation_url() for site_section in site_sections]
        expected_results = ['/data/', '/st/', '/modules/', '/pipelines/', '#']
        self.assertEqual(urls, expected_results)
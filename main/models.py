from django.db import models
from django.urls.base import reverse
from django.urls import NoReverseMatch

# Create your models here.
class NavigationSection(models.Model):
    DEFAULT_PATH_NAME = "#"
    id = models.IntegerField(primary_key=True, verbose_name='ID')
    display_text = models.CharField(max_length=30, verbose_name='Display Text', blank=True)
    icon_url = models.CharField(max_length=100, verbose_name='Icon URL', blank=True)
    navigation_path_name = models.CharField(max_length=100, default=DEFAULT_PATH_NAME, blank=True, verbose_name='Path Name')

    class Meta:
        abstract = True

    def get_navigation_url(self):
        try:
            return reverse(self.navigation_path_name)
        except NoReverseMatch as ex:
            return self.DEFAULT_PATH_NAME
    
    def __str__(self):
        return f'Section: {self.display_text}'

class SiteSection(NavigationSection):
    pass
    
class SidebarSection(NavigationSection):
    parent = models.ForeignKey('self', on_delete=models.SET_DEFAULT, default=-1, blank=True, null=True, unique=False, verbose_name='Parent')
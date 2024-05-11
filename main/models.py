from django.db import models
from django.urls.base import reverse
from django.urls import NoReverseMatch

# Create your models here.
class SiteSection(models.Model):
    DEFAULT_PATH_NAME = "#"
    id = models.IntegerField(primary_key=True, verbose_name='ID')
    display_text = models.CharField(max_length=30, verbose_name='Display Text')
    icon_url = models.CharField(max_length=100, verbose_name='Icon URL')
    navigation_path_name = models.CharField(max_length=100, default=DEFAULT_PATH_NAME, verbose_name='Path Name')

    def get_navigation_url(self):
        try:
            return reverse(self.navigation_path_name)
        except NoReverseMatch as ex:
            return self.DEFAULT_PATH_NAME
    
    def __str__(self):
        return f'Section: {self.display_text}'
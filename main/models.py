from django.db import models

# Create your models here.
class SiteSection(models.Model):
    id = models.IntegerField(primary_key=True)
    display_text = models.CharField(max_length=30)
    icon_url = models.CharField(max_length=100)
    #TODO: think of replacing navigation_url with relative path and create a method that returns `reverse` with the corresponding path name
    navigation_url = models.CharField(max_length=100, default='#')
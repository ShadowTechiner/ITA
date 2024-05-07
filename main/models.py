from django.db import models

# Create your models here.
class SiteSection(models.Model):
    id = models.IntegerField(primary_key=True)
    display_text = models.CharField(max_length=30)
    icon_url = models.CharField(max_length=100)
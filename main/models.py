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

class Platform(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='Platform ID')
    display_text = models.CharField(max_length=500, verbose_name='Platform Name')

    def __str__(self):
        return self.display_text

class Product(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='Product ID')
    display_text = models.CharField(max_length=500, verbose_name='Product Name')

    def __str__(self):
        return self.display_text

class Build(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='Build ID')
    display_text = models.CharField(max_length=10, verbose_name='Version')

    def __str__(self):
        return self.display_text

class OperationalSystem(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='ID')
    display_text = models.CharField(max_length=100, verbose_name='OS Name')

    def __str__(self):
        return self.display_text

class IDE(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='ID')
    display_text = models.CharField(max_length=100, verbose_name='IDE Name')

    def __str__(self):
        return self.display_text

class Ticket(models.Model):
    ticket_number = models.CharField(primary_key=True, max_length=20, verbose_name='Ticket Number')
    subject = models.TextField(verbose_name='Subject')
    creation_date = models.DateField(verbose_name='Date of Creation')
    platform = models.ForeignKey(Platform, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Platform')
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Product')
    build = models.ForeignKey(Build, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Build Version')
    operational_system = models.ForeignKey(OperationalSystem, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='OS')
    ide = models.ForeignKey(IDE, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='IDE')

    def __str__(self):
        return f'{self.ticket_number} : {self.subject}'

class Node:
    def __init__(self, section, children):
        self.section = section
        self.children = children
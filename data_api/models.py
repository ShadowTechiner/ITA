from django.db import models

# Create your models here.
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
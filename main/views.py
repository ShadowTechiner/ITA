from django.shortcuts import render
from django.http import HttpResponse
from .models import SiteSection

# Create your views here.
def index(request):
    context = { 'site_sections' :  SiteSection.objects.all() }
    return render(request, 'index.html', context=context)
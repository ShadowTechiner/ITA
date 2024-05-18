from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from .models import SiteSection, SidebarSection

# Create your views here.
class IndexView(TemplateView):

    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["site_sections"] = SiteSection.objects.all()
        return context

class DataTicketTableView(TemplateView):

    template_name = ''

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['site_sections'] = SiteSection.objects.all()
        context['sidebar_sections'] = SidebarSection.objects.all()
        
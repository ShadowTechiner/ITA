from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from .models import SiteSection, SidebarSection, Node

# Create your views here.
class IndexView(TemplateView):

    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["site_sections"] = SiteSection.objects.all()
        return context
    
class DataView(TemplateView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['site_sections'] = SiteSection.objects.all()
        nodes = list()
        for sidebar_section in SidebarSection.objects.filter(parent__exact=None):
            node = Node(sidebar_section, SidebarSection.objects.filter(parent__exact=sidebar_section))
            nodes.append(node)
        context['sidebar_parent_sections'] = nodes
        return context

class DataTicketTableView(DataView):

    template_name = 'tickettable.html'

class DataTicketStatsView(DataView):

    template_name = 'ticketstats.html'

class DataPostTableView(DataView):

    template_name = 'posttable.html'

class DataPostStatsView(DataView):

    template_name = 'poststats.html'
        
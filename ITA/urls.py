"""
URL configuration for ITA project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from main.views import IndexView, DataTicketTableView, DataTicketStatsView, DataPostTableView, DataPostStatsView
from django.http import HttpResponse
from data_api.views import TicketListView, TicketView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('data-api/tickets', TicketListView.as_view(), name = 'get-tickets'),
    path('data-api/tickets/<slug:pk>', TicketView.as_view(), name='get-ticket'),
    path('', IndexView.as_view(), name='index'),
    path('data/tickets/table', DataTicketTableView.as_view(), name = 'data'),
    path('data/tickets/table', DataTicketTableView.as_view(), name = 'tickettable'),
    path('data/tickets/stats', DataTicketStatsView.as_view(), name = 'ticketstats'),
    path('data/posts/table', DataPostTableView.as_view(), name = 'posttable'),
    path('data/posts/stats', DataPostStatsView.as_view(), name = 'poststats'),
    path('st/', IndexView.as_view(), name = 'similartickets'),
    path('modules/', IndexView.as_view(), name = 'modules'),
    path('pipelines/', IndexView.as_view(), name = 'pipelines')
]

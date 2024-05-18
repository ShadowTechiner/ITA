from django.shortcuts import render, get_object_or_404
from django.views import View
from django.http import HttpResponse, JsonResponse
from .models import Ticket
from .serializers import TicketSerializer
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from django.middleware.csrf import get_token

# Create your views here.
class TicketListView(View):
    def get(self, request, *args, **kwargs):
        g = get_token(request)
        tickets = Ticket.objects.all()
        serializer = TicketSerializer(tickets, many=True)
        return JsonResponse(serializer.data, safe=False)

    def post(self, request, *args, **kwargs):
        #data = JSONParser().parse(request)
        serializer = TicketSerializer(data=request.POST)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    
class TicketView(View):
    def get(self, request, pk):
        try:
            ticket = Ticket.objects.get(pk=pk)
        except Ticket.DoesNotExist:
            return HttpResponse(status=404)
        serializer = TicketSerializer(ticket)
        return JsonResponse(serializer.data, safe=False)

    def put(self, request, pk):
        try:
            ticket = Ticket.objects.get(pk=pk)
        except Ticket.DoesNotExist:
            return HttpResponse(status=404)
        serializer = TicketSerializer(ticket, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        try:
            ticket = Ticket.objects.get(pk=pk)
        except Ticket.DoesNotExist:
            return HttpResponse(status=404)
        ticket.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
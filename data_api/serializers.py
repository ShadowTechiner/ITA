from rest_framework import serializers
from . import models

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Ticket
        fields = ['ticket_number', 'subject', 'creation_date', 'platform', 'product', 'build', 'operational_system', 'ide']

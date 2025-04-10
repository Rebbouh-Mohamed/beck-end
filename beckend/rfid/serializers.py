from rest_framework import serializers
from .models import RFID

class RFIDSerializer(serializers.ModelSerializer):
    class Meta:
        model = RFID
        fields = ['id_rfid', 'name', 'last_access', 'is_active']

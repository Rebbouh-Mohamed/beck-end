from rest_framework import serializers
from .models import SignalData

class SignalDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = SignalData
        fields = ['time', 'users', 'signal', 'freq_used']


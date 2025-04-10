from rest_framework import serializers
from .models import SignalData

class SignalDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = SignalData
        fields = ['user_count', 'time_of_day', 'signal_strength', 'traffic_type', 'rbs']

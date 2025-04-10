from rest_framework import serializers
from .models import Material

class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = ['id', 'name', 'last_maintenance', 'next_maintenance', 'status', 'time_left']

from rest_framework import serializers
from .models import SystemStat

class SystemStatSerializer(serializers.ModelSerializer):
    class Meta:
        model = SystemStat
        fields = '__all__'

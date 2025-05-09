from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import LogEntry
from .serializers import LogEntrySerializer

class LogEntryAPIView(APIView):

    def get(self, request):
        logs = LogEntry.objects.all().order_by('-timestamp')
        serializer = LogEntrySerializer(logs, many=True)
        return Response(serializer.data)

    def post(self, request):
        
        serializer = LogEntrySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

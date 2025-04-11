from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import RFID
from .serializers import RFIDSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser,AllowAny
from datetime import datetime

class RFIDListView(APIView):
    permission_classes = [IsAuthenticated]  # Only authenticated users can access this view

    def get(self, request):
        rfid_data = RFID.objects.all()  # Get all RFID records
        serializer = RFIDSerializer(rfid_data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class RFIDCreateView(APIView):
    permission_classes = [AllowAny]  # Only admins can create new RFID entries

    def post(self, request):
        # Deserialize the incoming data
        serializer = RFIDSerializer(data=request.data)
        
        if serializer.is_valid():
            # Save the RFID entry to the database
            rfid = serializer.save()
            return Response({'message': 'RFID created successfully', 'data': serializer.data}, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RFIDUpdateAccessView(APIView):
    permission_classes = [IsAuthenticated]  # Only authenticated users can update last access

    def put(self, request, id_rfid):
        try:
            # Fetch the RFID record to update
            rfid = RFID.objects.get(id_rfid=id_rfid)
        except RFID.DoesNotExist:
            return Response({'error': 'RFID not found'}, status=status.HTTP_404_NOT_FOUND)

        # Update the last_access field
        rfid.last_access = datetime.now()
        rfid.save()

        return Response({'message': 'Last access updated successfully'}, status=status.HTTP_200_OK)

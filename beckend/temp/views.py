from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import SystemStat
from .serializers import SystemStatSerializer
from rest_framework.permissions import IsAuthenticated,AllowAny



class ListingStatView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        stats = SystemStat.objects.all().order_by('-timestamp')  # latest first
        serializer = SystemStatSerializer(stats, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    
    
class SystemStatView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        # Deserialize the incoming data
        serializer = SystemStatSerializer(data=request.data)
        
        if serializer.is_valid():
            # Save the instance to the database
            system_stat = serializer.save()

            # Perform custom calculations based on the saved data
            score = (
                system_stat.indoor_temp * 0.3 +
                system_stat.humidity * 0.1 +
                system_stat.server_load * 0.2 +
                system_stat.external_temp * 0.1 +
                system_stat.ac_level * 0.1 +
                system_stat.fans_active * 0.1 +
                system_stat.hour * 0.1
            )

            final_score = round(score)  # Example: rounding the final score

            # Return the calculated result
            return Response({'action': final_score}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
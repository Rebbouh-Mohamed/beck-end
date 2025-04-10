from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import SystemStat
from .serializers import SystemStatSerializer
from rest_framework.permissions import IsAuthenticated,AllowAny
from ai_model.ml import load_rl_model
import numpy as np 

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
            model=load_rl_model()
            # Perform custom calculations based on the saved data
            score = np.array(
                [system_stat.indoor_temp ,
                system_stat.humidity ,
                system_stat.server_load ,
                system_stat.external_temp ,
                system_stat.ac_level ,
                system_stat.fans_active ,
                system_stat.hour]
            )

            final_score = model.predict(score,deterministic=False)  # Example: rounding the final score
            final_score=final_score[0].astype(int)
            # Return the calculated result
            return Response({'action': final_score}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
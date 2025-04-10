import random
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import SignalData
from .serializers import SignalDataSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from ai_model.ml import load_rbs_model
import numpy as np

class SignalDataListView(APIView):
    permission_classes = [IsAuthenticated]  # Only authenticated users can list data

    def get(self, request):
        # Retrieve all SignalData entries, ordered by time_of_day (or any other sorting logic you prefer)
        signal_data = SignalData.objects.all().order_by('-time_of_day')
        serializer = SignalDataSerializer(signal_data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class SignalDataCreateView(APIView):
    permission_classes = [AllowAny]  # Anyone can post for now, change later if needed

    def post(self, request):
        # Deserialize the incoming data
        serializer = SignalDataSerializer(data=request.data)

        if serializer.is_valid():
            try:
                # Save the instance to the database
                signal_data = serializer.save()

                # Check if the rbs value exists; if not, perform random calculation
                if signal_data.rbs == 0:  # If rbs is 0, perform the random calculation
                    signal_data.rbs = random.randint(10, 100)  # Random number between 10 and 100
                    signal_data.save()
                model=load_rbs_model()
                    
                # Perform any custom logic for calculating 'new rbs'
                # Placeholder for your custom calculation logic, like using user_count, time_of_day, etc.
                data=np.array([
                    signal_data.user_count,
                    signal_data.time_of_day,
                    signal_data.signal_strength,
                    signal_data.traffic_type,
                ]).reshape(1,-1)
                new_rbs = model.predict(data)  # Example logic (you can replace this with your actual calculation)

                # Return the calculated result
                return Response({'new_rbs': new_rbs}, status=status.HTTP_200_OK)

            except Exception as e:
                return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

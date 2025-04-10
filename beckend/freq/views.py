from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import SignalData
from .serializers import SignalDataSerializer
import random
import numpy as np
from ai_model.ml import load_freq_model


class ListingSignalDataView(APIView):
    permission_classes = [IsAuthenticated]  # Anyone can access this view

    def get(self, request):
        try:
            # Retrieve and order by the latest time
            signal_data = SignalData.objects.all().order_by('-time')  
            serializer = SignalDataSerializer(signal_data, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class SignalDataView(APIView):
    permission_classes = [AllowAny]  # Only authenticated users can add data

    def post(self, request):
        # Deserialize the incoming data
        serializer = SignalDataSerializer(data=request.data)
        
        if serializer.is_valid():
            try:
                # Save the instance to the database
                signal_data = serializer.save()

                # Handle frequency (`freq_used`) if it exists, else calculate randomly
                try:
                    freq_used = signal_data.freq_used
                except AttributeError:  # freq_used does not exist
                    # Perform a random calculation if `freq_used` is missing
                    freq_used = random.randint(10, 100)  # Random number between 10 and 100
                model=load_freq_model()
                # Perform custom calculations based on the saved data
                score =np.array (
                    [signal_data.signal ,
                    signal_data.users ,
                    signal_data.time ,]
                ).reshape(1, -1)
                final_score=model.predict(score)[0]

                # Return the calculated result
                return Response({'new freq': final_score}, status=status.HTTP_200_OK)

            except Exception as e:
                return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

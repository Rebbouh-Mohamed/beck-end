from rest_framework import status, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated,AllowAny
from .models import Material
from .serializers import MaterialSerializer

# To handle adding and listing of materials (only auth users can access)
class MaterialListView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        materials = Material.objects.all()  # List all materials
        serializer = MaterialSerializer(materials, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

# To handle adding new material (only admin users can add)
class MaterialCreateView(APIView):
    permission_classes = [permissions.IsAdminUser]

    def post(self, request):
        serializer = MaterialSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# To handle updating a material's status, maintenance date, etc.
class MaterialUpdateView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, pk):
        try:
            material = Material.objects.get(pk=pk)
        except Material.DoesNotExist:
            return Response({"error": "Material not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = MaterialSerializer(material, data=request.data, partial=True)  # partial=True allows updating only specific fields
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

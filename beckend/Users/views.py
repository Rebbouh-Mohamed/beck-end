from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from django.contrib.auth.models import User
from .serializers import AdminUserCreateSerializer

class AdminUserCreateView(APIView):
    permission_classes = [permissions.IsAdminUser]  # Only admin access

    def get(self, request):
        users = User.objects.all()
        serializer = AdminUserCreateSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AdminUserCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

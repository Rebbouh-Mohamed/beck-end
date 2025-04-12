from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from django.contrib.auth.models import User
from .serializers import AdminUserCreateSerializer
from django.shortcuts import get_object_or_404

class AdminUserCreateView(APIView):
    permission_classes = [permissions.IsAdminUser]

    def get(self, request):
        users = User.objects.all()
        serializer = AdminUserCreateSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        print(request.data)
        serializer = AdminUserCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        if not pk:
            return Response({"error": "User ID is required for update."}, status=status.HTTP_400_BAD_REQUEST)

        user = get_object_or_404(User, pk=pk)
        serializer = AdminUserCreateSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        if not pk:
            return Response({"error": "User ID is required for deletion."}, status=status.HTTP_400_BAD_REQUEST)

        user = get_object_or_404(User, pk=pk)
        user.delete()
        return Response({"message": f"User with ID {pk} has been deleted."}, status=status.HTTP_204_NO_CONTENT)

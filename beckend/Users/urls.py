from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import AdminUserCreateView 



urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('admin/users/', AdminUserCreateView.as_view()),         # GET, POST
    path('admin/users/<int:pk>/', AdminUserCreateView.as_view()) # PUT, DELETE
    
]
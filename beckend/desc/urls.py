from django.urls import path
from .views import LogEntryAPIView

urlpatterns = [
    path('logs/', LogEntryAPIView.as_view(), name='log-entry-api'),
]

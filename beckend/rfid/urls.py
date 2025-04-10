from django.urls import path
from .views import RFIDListView, RFIDCreateView, RFIDUpdateAccessView

urlpatterns = [
    path('list/', RFIDListView.as_view(), name='rfid-list'),
    path('create/', RFIDCreateView.as_view(), name='rfid-create'),
    path('update-access/<str:id_rfid>/', RFIDUpdateAccessView.as_view(), name='rfid-update-access'),
]

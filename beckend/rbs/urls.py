from django.urls import path
from .views import SignalDataListView, SignalDataCreateView

urlpatterns = [
    path('list-signal-data/', SignalDataListView.as_view(), name='signal-data-list'),  # GET: List all SignalData instances
    path('add-signal-data/', SignalDataCreateView.as_view(), name='signal-data-create'),  # POST: Add a new SignalData
]

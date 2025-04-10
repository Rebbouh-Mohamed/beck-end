from django.urls import path
from .views import ListingSignalDataView, SignalDataView

urlpatterns = [
    path('list-signal-data/', ListingSignalDataView.as_view(), name='list_signal_data'),  # Listing all SignalData
    path('add-signal-data/', SignalDataView.as_view(), name='add_signal_data'),  # Adding new SignalData
]

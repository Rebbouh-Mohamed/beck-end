from django.urls import path
from .views import ListingStatView,SystemStatView

urlpatterns = [
    path('add-stats/', SystemStatView.as_view(), name='system-stats'),
    path('list-stats/', ListingStatView.as_view(), name='system-stats'),

]

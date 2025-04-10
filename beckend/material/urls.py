from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.MaterialListView.as_view(), name='material-list'),
    path('create/', views.MaterialCreateView.as_view(), name='material-create'),
    path('<int:pk>/update/', views.MaterialUpdateView.as_view(), name='material-update'),
]
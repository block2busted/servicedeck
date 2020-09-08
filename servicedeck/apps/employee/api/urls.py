from django.urls import path
from .views import (
    EmployeeListAPI,
    EmployeeDetailAPIView
)

urlpatterns = [
    path('', EmployeeListAPI.as_view(), name='employee-list'),
    path('<int:pk>/', EmployeeDetailAPIView.as_view(), name='employee-detail'),
]
from django.urls import path
from .views import (
    EmployeeListAPI,
    EmployeeDetailAPIView,
    EmployeeSignUpAPIView
)

urlpatterns = [
    path('', EmployeeListAPI.as_view(), name='employee-list'),
    path('<int:pk>/', EmployeeDetailAPIView.as_view(), name='employee-detail'),
    path('sign_up/', EmployeeSignUpAPIView.as_view(), name='employee-sign-up')
]
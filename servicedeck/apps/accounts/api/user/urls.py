from django.urls import path
from .views import UserDetailAPIView, UserEmployeeAPIView


urlpatterns = [
    path('<str:username>/', UserDetailAPIView.as_view(), name='user-detail'),
    path('<str:username>/employee/', UserEmployeeAPIView.as_view(), name='user-list')
]
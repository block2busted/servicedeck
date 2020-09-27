from django.urls import path
from .views import (
    WorkCreateAPIView,
    WorkDetailAPIView,
    WorkListAPIView,
    WorkStartAPIView,
    WorkInProcessAPIView
)


urlpatterns = [
    path('', WorkListAPIView.as_view(), name='work-create'),
    path('create/', WorkCreateAPIView.as_view(), name='work-list'),
    path('<int:pk>/', WorkDetailAPIView.as_view(), name='work-detail'),
    path('<int:pk>/start/', WorkStartAPIView.as_view(), name='work-start'),
    path('in_process/', WorkInProcessAPIView.as_view(), name='')

]
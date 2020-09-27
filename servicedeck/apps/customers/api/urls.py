from django.urls import path
from .views import CustomerSignUpAPIView


urlpatterns = [
    path('sign_up/', CustomerSignUpAPIView.as_view(), name='sign-up')
]
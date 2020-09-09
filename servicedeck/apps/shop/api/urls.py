from django.urls import path
from .views import ShopApiView, ShopCreateAPIView


urlpatterns = [
    path('', ShopApiView.as_view()),
    path('create/', ShopCreateAPIView.as_view(), name='')
]
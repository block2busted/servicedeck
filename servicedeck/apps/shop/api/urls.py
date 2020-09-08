from django.urls import path
from .views import ShopApiView


urlpatterns = [
    path('', ShopApiView.as_view())
]
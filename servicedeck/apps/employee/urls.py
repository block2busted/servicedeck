from django.contrib import admin
from django.urls import path
from .views import update_employee_detail_view


app_name = 'shop'
urlpatterns = [
    path('', update_employee_detail_view, name='update_model')
]

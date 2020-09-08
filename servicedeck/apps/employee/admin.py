from django.contrib import admin
from .models import Employee, Position
from .forms import EmployeeForm


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'middle_name', 'last_name', 'kpi']
    form = EmployeeForm

    class Meta:
        model = Employee


admin.site.register(Employee, EmployeeAdmin)

admin.site.register(Position)

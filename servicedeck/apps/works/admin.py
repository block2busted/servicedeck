from django.contrib import admin

from .models import Work, EmployeeWork


admin.site.register(Work)

admin.site.register(EmployeeWork)
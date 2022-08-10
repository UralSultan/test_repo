from django.contrib import admin
from .models import Department, Employee, EmployeePosition, Tutor

admin.site.register(Department)
admin.site.register(EmployeePosition)
admin.site.register(Employee)
admin.site.register(Tutor)

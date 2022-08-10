from django.contrib import admin
from .models import Student, StudentCourse

admin.site.register(StudentCourse)
admin.site.register(Student)

from .models import Student, StudentCourse
from django.forms import ModelForm


class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'date_of_birth', 'school', 'is_active', 'is_graduate']


class StudentCourseForm(ModelForm):
    class Meta:
        model = StudentCourse
        fields = ['student', 'course']

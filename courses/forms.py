from .models import Course
from django import forms
# from school.schools_app.models import School


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'school', 'is_active', 'price', 'duration', 'max_student']

#
# class CoursesForm(forms.Form):
#     school = forms.ModelChoiceField(queryset=School.objects.all())

from django.db import models
from django.contrib.auth.models import User


class Department(models.Model):
    department_name = models.CharField(max_length=255)
    description = models.TextField()
    school = models.ForeignKey('schools_app.School', on_delete=models.PROTECT, related_name='departments')

    def __str__(self):
        return self.department_name


class EmployeePosition(models.Model):
    name = models.CharField(max_length=50)
    department = models.ForeignKey(Department, on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.name


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='employee')
    date_of_birth = models.DateField()
    image = models.ImageField()
    position = models.ForeignKey(EmployeePosition, on_delete=models.PROTECT)
    salary = models.DecimalField(max_digits=7, decimal_places=2)

    # def __str__(self):
    #     return f'{self.user.first_name} '


class Tutor(models.Model):
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE, related_name='tutor')
    experience = models.PositiveSmallIntegerField()
    course = models.ForeignKey('courses.Course', on_delete=models.PROTECT, related_name='tutors')

    def __str__(self):
        return self.employee

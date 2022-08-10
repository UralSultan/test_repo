from django.db import models
# from school.courses.models import CourseModels
# from school.schools_app.models import SchoolModel


class Student(models.Model):
    name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    email = models.EmailField(null=True, default=None)
    school = models.ForeignKey('schools_app.School', on_delete=models.PROTECT)
    is_active = models.BooleanField(default=False)
    is_graduate = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class StudentCourse(models.Model):
    student = models.ForeignKey(Student, on_delete=models.PROTECT)
    course = models.ForeignKey('courses.Course', on_delete=models.PROTECT)
    score = models.PositiveSmallIntegerField(null=True, default=None)

    def __str__(self):
        return f"({self.student}/{self.course}/{self.score}"

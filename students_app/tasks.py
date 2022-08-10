from celery import shared_task
from django.core.mail import send_mail
from django.db.models import Avg

from .models import StudentCourse, Student
import json


@shared_task
def send_message_to_student(**kwargs):
    send_mail(**kwargs)

"""
запрос в ручную
@shared_task
def log_students_avg_score():
    scores_dict = {}
    students = Student.objects.all()
    for student in students:
        courses = StudentCourse.objects.filter(student=student)
        score = 0
        for course in courses:
            score += course.score
            scores_dict[student.id] = [student.name, score / len(courses)]

    with open('student_score.csv', 'w') as f:
        for key, value in scores_dict.items():
            f.write(f'{key}, {value[0]}, {value[1]}\n')
"""


@shared_task
def log_students_avg_score():
    scores_dict = {}
    avg_scores = StudentCourse.objects.values('student__id', 'student__name').annotate(avg_score=Avg('score'))

    with open('student_avg_score.csv', 'w') as file:
        for score in avg_scores:
            file.write(f'{score["student__id"]}, {score["student__name"]}, {score["avg_score"]} \n')
    print("END of task")

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from .models import Student, StudentCourse
from .tasks import send_message_to_student


@receiver(post_save, sender=Student)
def student_created(sender, instance, created, **kwargs):
    if created:
        subject = 'Hello message/do not reply'
        message = f'Dear {instance.name}. Welcome to our school'
        from_email = settings.EMAIL_HOST_USER
        to_list = [instance.email]
        # send_mail(
        #     subject=subject, message=message, from_email=from_email, recipient_list=to_list, fail_silently=False
        # )
        send_message_to_student.delay(
            subject=subject, message=message, from_email=from_email, recipient_list=to_list, fail_silently=False
        )


@receiver(post_save, sender=StudentCourse)
def students_av_score(sender, instance, created, **kwargs):
    if created:
        scores_dict = {}
        students = Student.objects.all()
        for student in students:
            courses = StudentCourse.objects.filter(student=student)
            score = 0
            for course in courses:
                score += course.score
                scores_dict[student.id] = [student.name, score / len(courses)]

        with open('student_score1.csv', 'w') as f:
            for key, value in scores_dict.items():
                f.write(f'{key}, {value[0]}, {value[1]}\n')

import random

from rest_framework import serializers
from .models import Student, StudentCourse
from schools_app.serializer import SchoolSerializer
# from schools_app.models import School
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

"""
class StudentSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=255)
    date_of_birth = serializers.DateField()
    school = serializers.PrimaryKeyRelatedField(queryset=School.objects.all())
    is_active = serializers.BooleanField(default=False)
    is_graduate = serializers.BooleanField(default=False)

    def create(self, validated_data):
        # путь короче
        student = Student.objects.create(**validated_data)
        # путь расшифрованный
        # course = Course.objects.create(
        #     name=validated_data['name'],
        #     school=validated_data['school'],
        #     is_active=validated_data['is_active'],
        #     price=validated_data['price'],
        #     duration=validated_data['duration'],
        #     max_student=validated_data['max_student']
        # )
        return student

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.date_of_birth = validated_data.get('date_of_birth', instance.date_of_birth)
        instance.school = validated_data.get('school', instance.school)
        instance.is_active = validated_data.get('is_active', instance.is_active)
        instance.is_graduate = validated_data.get('is_graduate', instance.is_graduate)
        instance.save()
        return instance
"""


class StudentSerializer(serializers.ModelSerializer):
    average_score = serializers.IntegerField(read_only=True, default=None)
    email = serializers.EmailField(required=True)

    class Meta:
        model = Student
        fields = ['id', 'name', 'date_of_birth', 'email', 'school', 'is_active', 'is_graduate', 'average_score']

    # def create(self, validated_data):
    #     student = super().create(validated_data)
    #     subject = 'Hello message/do not reply'
    #     message = f'Dear {student.name}. Welcome to our school'
    #     from_email = settings.EMAIL_HOST_USER
    #     to_list = [student.email]
    #     send_mail(
    #         subject=subject, message=message, from_email=from_email, recipient_list=to_list, fail_silently=True
    #     )
    #     return student

    def to_representation(self, instance):
        response = super().to_representation(instance)
        serializers_school = SchoolSerializer(instance=instance.school)
        student_courses = StudentCourse.objects.filter(student=instance)
        score = 0
        len_of_items = 0
        for student_course in student_courses:
            score += student_course.score
            len_of_items += 1

        if len_of_items != 0:
            response['average_score'] = score / len_of_items
        response["school"] = serializers_school.data

        return response

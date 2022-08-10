from rest_framework import serializers
from .models import Course
from schools_app.serializer import SchoolSerializer
from rest_framework.validators import UniqueTogetherValidator


class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = ['name', 'school', 'is_active', 'price', 'duration', 'max_student']
        validators = [
            UniqueTogetherValidator(
                queryset=Course.objects.all(),
                fields=['name', 'school']
            )
        ]

    def to_representation(self, instance):
        response = super().to_representation(instance)
        serializers_school = SchoolSerializer(instance=instance.school)
        response["school"] = serializers_school.data
        return response

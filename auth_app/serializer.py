from django.contrib.auth.models import User
from employees.models import EmployeePosition, Employee
from rest_framework import serializers, validators
from rest_framework.authtoken.models import Token


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    email = serializers.EmailField(
        required=True,
        validators=[validators.UniqueValidator(queryset=User.objects.all())])
    username = serializers.CharField(
        required=True,
        validators=[validators.UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField(required=True, min_length=8, write_only=True)
    confirm_password = serializers.CharField(required=True, min_length=8, write_only=True)
    date_of_birth = serializers.DateField(write_only=True)
    image = serializers.ImageField(required=False, allow_null=True, write_only=True)
    position = serializers.PrimaryKeyRelatedField(queryset=EmployeePosition.objects.all(), write_only=True)
    salary = serializers.DecimalField(max_digits=7, decimal_places=2, write_only=True)

    def validate(self, attrs):
        attrs = super().validate(attrs)
        password = attrs['password']
        confirm_password = attrs['confirm_password']
        if password != confirm_password:
            raise serializers.ValidationError(detail='password does not match', code='password_match')
        return attrs

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"],
            password=validated_data["password"]
        )
        Employee.objects.create(
            user=user,
            date_of_birth=validated_data['date_of_birth'],
            image=validated_data['image'],
            position=validated_data['position'],
            salary=validated_data['salary'],
        )
        # Token.objects.create(user=user)
        return user

    def to_representation(self, instance):
        response = super().to_representation(instance)
        token = Token.objects.filter(user_id=instance.id).first()
        response['token'] = token.key
        return response

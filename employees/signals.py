import json

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token
from django.dispatch import receiver
from .models import Employee


@receiver(post_save, sender=User)
def user_created(sender, instance, created, **kwargs):
    if created:
        Token.objects.create(user=instance)


@receiver(post_save, sender=Employee)
def save_data(sender, instance, created, **kwargs):
    if created:
        employee = {
            'date_of_birth': instance.date_of_birth,
            'position': instance.position,
            'salary': instance.salary,
        }
        with open('text1.json', 'a') as f:
            f.write(json.dumps(employee, indent=4, sort_keys=True, default=str))

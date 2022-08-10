from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User


def user_create(sender, **kwargs):
    print(sender)
    print(**kwargs)


post_save.connect(user_create, sender=User)

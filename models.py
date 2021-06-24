from django.db import models

from django.contrib.auth import get_user_model


User = get_user_model()
import uuid


# Create your models here.
class Company(models.Model):
    user = models.ForeignKey(
        User, related_name="user_name", on_delete=models.PROTECT
    )
    company_name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
from django.db import models
from django.contrib.auth.models import User
import datetime

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, null=True)
    description = models.TextField(null=True)
    date = models.DateField(null=True, default=datetime.date.today)
    is_finished = models.BooleanField(default=False)
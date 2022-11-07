from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, blank=False)
    description = models.CharField(max_length=555)
    task_date = models.DateField(auto_now=False, blank=False)
    task_hour = models.TimeField(auto_now=False, blank=True)
    created_at = models.DateField(auto_now=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
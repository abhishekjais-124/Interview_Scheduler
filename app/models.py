from django.db import models
from django.contrib.auth.models import User


class Users(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=50, unique=True)


class Interviews(models.Model):
    startTime = models.DateTimeField()
    endTime = models.DateTimeField()


class UserInterviews(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    interview = models.ForeignKey(Interviews, on_delete=models.CASCADE)

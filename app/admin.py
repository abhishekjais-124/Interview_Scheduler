from django.contrib import admin

from .models import (Users, Interviews, UserInterviews)


@admin.register(Users)
class UsersModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email']


@admin.register(Interviews)
class InterviewsModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'startTime', 'endTime']


@admin.register(UserInterviews)
class UserInterviewsModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'interview']

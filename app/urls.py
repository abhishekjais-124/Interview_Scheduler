from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('', views.DashboardView.as_view(), name="dashboard"),
    path('interviews/', views.InterviewsClass.as_view(), name="interviews"),
    path('update/', views.update, name="update"),
    path('<int:id>/', views.update_data, name="updatedata"),

]

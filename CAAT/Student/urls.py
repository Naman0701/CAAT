
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path("ATTENDANCE/",views.Attend,name="Attendance"),
    path("ATTENDANCE/<subject>",views.Attendance_Subject,name="Attendance_Subject"),
    path("AICTE/",views.aicte,name="aicte"),
    ]
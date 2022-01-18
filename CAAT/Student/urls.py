
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path("ATTENDANCE/",views.Attendance,name="Attendance"),
    path("AICTE/",views.aicte,name="aicte"),
    ]
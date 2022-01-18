
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.login,name="Log_IN"),
    path("home/",views.home,name="home"),
    path("home/Student/", include('Student.urls'))
]

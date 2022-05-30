from django.contrib import admin
from .models import Student,Teacher,Teaches,Subject,Attendance,Mentor,AicteP
# Register your models here.

class AdminS(admin.ModelAdmin):
    list_display = ['Usn','Fname','Lname']

class AdminT(admin.ModelAdmin):
    list_display = ['Ssn','Fname','Lname']

class AdminSu(admin.ModelAdmin):
    list_display = ['Sub_code','Sub_name']

class AdminTs(admin.ModelAdmin):
    list_display = ['Teacher_id','Sub_code','Dept','Sem','Sec']

class AdminA(admin.ModelAdmin):
    list_display = ['Date','Usn','Sub_code','Mark']
class AdminM(admin.ModelAdmin):
    list_display = ['mentor_d','Usn']
class AdminAicte(admin.ModelAdmin):
    list_display = ['Date','Usn']

admin.site.register(Student,AdminS)
admin.site.register(Teacher,AdminT)
admin.site.register(Teaches,AdminTs)
admin.site.register(Subject,AdminSu)
admin.site.register(Attendance,AdminA)
admin.site.register(Mentor,AdminM)
admin.site.register(AicteP,AdminAicte)

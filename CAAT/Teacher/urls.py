
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path("ATTENDANCE/",views.Attend,name="Attendance"),
    path("ATTENDANCE/enter/<sub>/<dept>/<sem>/<sec>",views.en_Attend,name="Attendance_enter"),
    path("ATTENDANCE/enter/<sub>/<dept>/<sem>/<sec>/submit",views.done_Attend,name="Attendance_done"),
    path("ATTENDANCE/edit/<sub>/<dept>/<sem>/<sec>/<dat>/update",views.up_attend,name="Attendance_up"),
    path("ATTENDANCE/view/<sub>/<dept>/<sem>/<sec>",views.v_Attend,name="Attendance_view"),
    path("ATTENDANCE/edit/<sub>/<dept>/<sem>/<sec>",views.e_Attend,name="Attendance_edit"),
    path("ATTENDANCE/del/<sub>/<dept>/<sem>/<sec>/<dat>",views.del_Attend,name="Attendance_del"),
    path("ATTENDANCE/cdel/<sub>/<dept>/<sem>/<sec>/<dat>",views.cdel_Attend,name="Attendance_cdel"),
    path("ATTENDANCE/edit/<sub>/<dept>/<sem>/<sec>/<dat>",views.ed_Attend,name="Attendance_edit_a"),
    path("ATTENDANCE/add/<sub>/<dept>/<sem>/<sec>",views.add_attend,name="Attendance_add"),
    path("ATTENDANCE/add/submit/<sub>/<dept>/<sem>/<sec>",views.add_sub_attend,name="Attendance_sub_add"),

    path("AICTE/",views.aicte,name="aicte"),
    path("AICTE/view/<usn>",views.v_aicte,name="v_aicte"),
    path("AICTE/view/<usn>/<isd>",views.d_aicte,name="d_aicte"),
    path("AICTE/del/<usn>/<isd>",views.cd_aicte,name="cd_aicte"),
    path("AICTE/enter/<usn>",views.a_aicte,name="a_aicte"),
    path("AICTE/enter/<usn>/submit",views.a_aicte_done,name="a_aicte_done"),

    ]
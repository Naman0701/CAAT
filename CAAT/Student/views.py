from django.shortcuts import render,redirect,HttpResponse
from Home.models import Student,Teacher,Subject,Attendance,Mentor,AicteP
from django.contrib.auth.models import User,auth

def Attend(req):
    class box:
        c_id: str
        c_name: str
        ac: int
        tc: int
        ap: int
        col: str
    b=[]
    id=req.session['id']
    data=Student.objects.filter(Usn=id)
    Sem=data.get().Sem
    Dept=data.get().Dept
    Sub=Subject.objects.filter(Sem=Sem).filter(Dept=Dept)
    Atd=Attendance.objects.filter(Usn=id)
    tc=0
    ac=0
    ap=0
    for i in Sub:
        obj=box()
        obj.c_id=i.Sub_code
        obj.c_name=i.Sub_name
        a=Attendance.objects.filter(Usn=id).filter(Sub_code=i.Sub_code)
        for j in a:
            tc+=1
            if j.Mark==True:
                ac+=1
        try:
            ap=round(ac/tc*100,2)
        except ZeroDivisionError:
            ap=0
        obj.col='#007300'
        if ap<75:
            obj.col='#d00000'
        obj.tc=tc
        obj.ac=ac
        obj.ap=ap
        tc=0
        ac=0
        b.append(obj)
    d={
        'b':b,
    'name': data.get().Fname + ' ' + data.get().Lname,
    }
    return render(req,'S_attendance.html',d)

def Attendance_Subject(req,subject):
    b=[]
    class box:
        date:str
        img:str
    id = req.session['id']
    data = Student.objects.filter(Usn=id)
    sub= Subject.objects.filter(Sub_name=subject)
    code=sub.get().Sub_code
    atd=Attendance.objects.filter(Usn=id).filter(Sub_code=code).order_by('-Date')
    for i in atd:
        mark='tick.png'
        if i.Mark==False:
            mark='x.png'
        obj=box()
        obj.date=i.Date
        obj.img=mark
        b.append(obj)
    d={
        'b':b,
        'name': data.get().Fname + ' ' + data.get().Lname,
        'sub':sub.get().Sub_name
    }
    return render(req,'attend_subject.html',d)


def aicte(req):
    b=[]
    class box:
        name:str
        point:int
    sum=0
    id = req.session['id']
    data = Student.objects.filter(Usn=id)
    m_name= f'{Mentor.objects.filter(Usn=id).get().Mentor.Fname} {Mentor.objects.filter(Usn=id).get().Mentor.Lname}'
    allwork=AicteP.objects.filter(Usn=id).order_by('-Date')
    for j in allwork:
        obj=box()
        obj.name=j.Activity
        obj.point=j.Point
        sum+=j.Point
        b.append(obj)
    Ment=Mentor.objects.get(Usn=id)
    Ment.Points=sum
    Ment.save()
    d={
        'b':b,
        'id':id,
        'name':data.get().Fname + ' ' + data.get().Lname,
        'm_name':m_name,
        'sum':Ment.Points
    }
    return render(req,'Aicte.html',d)

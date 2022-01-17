from django.shortcuts import render,redirect
from .models import Student,Teacher
from django.contrib.auth.models import User,auth

class box:
    name: str
    img : str
    title: str
    desc: str

def register(req):
    id = req.POST.get('id')
    pwd = req.POST.get('pwd')
    role = req.POST.get('role', 'off')
    if role=='on':
        staff=True
        data=Teacher.objects.filter(Ssn=id)
    else:
        staff = False
        data=Student.objects.filter(Usn=id)
    if data.exists():
        if not User.objects.filter(username=id).exists():
            user=User.objects.create_user(username=id,
                                          password=pwd,
                                          email=data.get().Email,
                                          first_name=data.get().Fname,
                                          last_name=data.get().Lname,
                                          is_staff=staff)
            user.save()
        else:
            print('USER ALREADY REGISTERED')
    else:
        print('USER DOES NOT EXIST')



def login(req):
    if req.method== 'POST':
        action = req.POST.get('action')
        if action == 'log_in':
            return render(req, 'home.html')
        elif action== 'register':
            register(req)
            return redirect('/')
    else:
        return render(req,'login.html')

def home(req):
    id = req.POST.get('id')
    pwd = req.POST.get('pwd')
    user=auth.authenticate(username=id, password=pwd)
    at = ('Enter the attendance of the students.', 'View your attendance.')
    ai = ('Enter the AICTE points of the students based on the activites attended.',
          'View your AICTE points based on the activites attended.')
    if user is not None:
        data=User.objects.filter(username=id)
        role=data.get().is_staff
        i = 1
        if role ==True:
            i = 0
        b1 = box()
        b1.img = 'attend.jpg'
        b1.title = 'ATTENDANCE'
        b1.desc = at[i]

        b2 = box()
        b2.img = 'AICTE.png'
        b2.title = 'AICTE'
        b2.desc = ai[i]

        b = [b1, b2]

        d = {'b': b,
             'name': data.get().first_name + ' ' + data.get().last_name
             }
        return render(req, 'home.html', d)
    else:
        print('INVALID')
        redirect('/')
    return redirect('/')


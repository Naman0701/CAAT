from django.shortcuts import render
from .models import Student,Teacher

class box:
    name: str
    img : str
    title: str
    desc: str

def login(req):
    if req.method== 'POST':
        return render(req, 'home.html')
    else:
        return render(req,'login.html')

def home(req):
    ssn = req.POST.get('usn')
    pwd = req.POST.get('pwd')
    role = req.POST.get('role', 'off')
    data = Student.objects.filter(Usn=ssn)
    at = ('Enter the attendance of the students.', 'View your attendance.')
    ai = ('Enter the AICTE points of the students based on the activites attended.',
          'View your AICTE points based on the activites attended.')
    i = 1
    if role == 'on':
        i = 0
    if ssn == '1JS19CS093' and pwd == 'Iloveu3000':
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
             'name': data.get().Fname + ' ' + data.get().Lname
             }
        return render(req, 'home.html', d)
    d = {
        'error': "Invalid username or password.Please try again"
    }
    return render(req, 'login.html', d)


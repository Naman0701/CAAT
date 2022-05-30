from django.db import models
# Create your models here.
class Student(models.Model):
    Usn=models.CharField(max_length=10,primary_key=True)
    Fname=models.CharField(max_length=25)
    Lname=models.CharField(max_length=25)
    Email=models.EmailField(max_length=30)
    Dept=models.CharField(max_length=50)
    Sem=models.IntegerField()
    Section=models.CharField(max_length=1)

    def __str__(self):
        id=self.Usn+' - '+ self.Fname+' '+self.Lname
        return id

class Teacher(models.Model):
    Ssn=models.CharField(max_length=10,primary_key=True)
    Fname=models.CharField(max_length=25)
    Lname=models.CharField(max_length=25)
    Email=models.EmailField(max_length=30)
    Dept=models.CharField(max_length=50)

    def __str__(self):
        id=self.Ssn+' - '+ self.Fname+' '+self.Lname
        return id

class Subject(models.Model):
    Sub_code=models.CharField(max_length=10,primary_key=True)
    Sub_name=models.CharField(max_length=50)
    Dept=models.CharField(max_length=50)
    Sem=models.IntegerField()
    Credits=models.IntegerField()

    def __str__(self):
        id=self.Sub_code+' - '+self.Sub_name
        return id

class Teaches(models.Model):
    Teacher_id=models.ForeignKey(Teacher,null=True,on_delete=models.SET_NULL)
    Sub_code=models.ForeignKey(Subject,null=True,on_delete=models.SET_NULL)
    Dept=models.CharField(max_length=50)
    Sem=models.IntegerField()
    Sec=models.CharField(max_length=1)
    def __str__(self):
        id=f'{self.Sub_code}-{self.Teacher_id}'
        return id

class Attendance(models.Model):
    Usn=models.ForeignKey(Student,on_delete=models.CASCADE)
    Sub_code=models.ForeignKey(Subject,on_delete=models.CASCADE)
    Date=models.DateField()
    Mark=models.BooleanField(default=True)
    def __str__(self):
        id=f'{self.Usn}-{self.Sub_code}-{self.Date}-{self.Mark}'
        return id
class Mentor(models.Model):
    Usn = models.ForeignKey(Student, on_delete=models.CASCADE)
    mentor_d= models.ForeignKey(Teacher,null=True,on_delete=models.SET_NULL)
    Points=models.IntegerField()
    def __str__(self):
        id=f'{self.Usn}-{self.mentor_d}'
        return id
class AicteP(models.Model):
    Usn=models.ForeignKey(Student,on_delete=models.CASCADE)
    Date=models.DateField()
    Activity=models.CharField(max_length=50)
    Point=models.IntegerField(default=0)




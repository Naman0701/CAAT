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
    Batch=models.IntegerField()

class Teacher(models.Model):
    Ssn=models.CharField(max_length=10,primary_key=True)
    Fname=models.CharField(max_length=25)
    Lname=models.CharField(max_length=25)
    Email=models.EmailField(max_length=30)
    Dept=models.CharField(max_length=50)


from django.db import models

# Create your models here.


class Student(models.Model):
    student=models.CharField(max_length=100)
    age=models.IntegerField()
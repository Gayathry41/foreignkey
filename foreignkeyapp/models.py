from django.db import models

# Create your models here.
class course(models.Model):
    course_name=models.CharField(max_length=200)
    fee=models.IntegerField(null=True)
    def __str__(self):
         return self.course_name

class student(models.Model):
    course=models.ForeignKey(course,on_delete=models.CASCADE,null=True)
    student_name=models.CharField(max_length=200)
    student_address=models.CharField(max_length=200)
    student_age=models.IntegerField(null=True,blank=True)
    joining_date=models.DateField(null=True)
    def __str__(self):
         return self.student_name
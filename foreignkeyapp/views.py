from django.shortcuts import render,redirect
from foreignkeyapp.models import course
from foreignkeyapp.models import student

# Create your views here.
def home(request):
    return render(request,'home.html')
def addcourse(request):
    return render(request,'addcourse.html')
def addcoursedb(request):
    if request.method=='POST':
        course_name=request.POST.get('course_name')
        fee=request.POST.get('fee')
        Course=course(course_name=course_name,fee=fee)
        Course.save()
        return redirect('/')

def addstudent(request):
    courses=course.objects.all()
    return render(request,'addstudent.html',{'course':courses})

def addstudentdb(request):
    if request.method=='POST':
        student_name=request.POST['student_name']
        student_address=request.POST['student_address']
        student_age=request.POST['student_age']
        joining_date=request.POST['joining_date']
        ok=request.POST['ok']
        course1=course.objects.get(id=ok)
        sttudent=student(student_name=student_name,student_address=student_address,student_age=student_age,joining_date=joining_date,course=course1)
        sttudent.save()
        return redirect('/')

def showstd(request):
    std=student.objects.all()
    return render(request,'showstudentdetails.html',{'students':std})
def edit(request,pk):
    studentt=student.objects.get(id=pk)
    courses=course.objects.all()
    
    return render(request,'edit.html',{'s':studentt,'k':courses})
def editdb(request,pk):
    if request.method=='POST':
      studentt=student.objects.get(id=pk)
      studentt.student_name=request.POST.get('student_name')
      studentt.student_address=request.POST.get('student_address')
      studentt.student_age=request.POST.get('student_age')
      studentt.joining_date=request.POST.get('joining_date')
      ok=request.POST.get('ok')
      studentt.course=course.objects.get(id=ok)
      studentt.save()
     
     
      return redirect('showstd')
    
    

    
def delete(request,pk):
    e=student.objects.get(id=pk)
    e.delete()
    
    return redirect('showstd')
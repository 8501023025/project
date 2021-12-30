from django.shortcuts import render
from django.http import HttpResponse
from .models import Employee

# Create your views here.
def empDetails(request):
   return render(request, 'empdetails.html')

def dateils(request):
   if request.method == 'POST':
      eno =request.POST['no']
      ename =request.POST['name']
      salary =request.POST['salary']
          
      emp = Employee()
          
      emp.empno =eno
      emp.empname =ename
      emp.empsalary =salary
          
      emp.save()
      print(eno,ename,salary)
          
          
   return render(request,'result.html')


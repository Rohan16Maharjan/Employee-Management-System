from django.shortcuts import render,redirect
from .forms import EmployeeForm,RegisterForm
from .models import Employee
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import  login,authenticate,logout
from django.contrib import messages


# Create your views here.

def home(request):
  return render(request,'EmployeeApp/home.html')

def depart(request):
  return render(request,'EmployeeApp/depart.html')

def emp(request):
  return render(request,'EmployeeApp/emp.html')

def addEmployee(request):
  form = EmployeeForm()
  if request.method == 'POST':
    form = EmployeeForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('home')
  context = {'form':form}
  return render(request,'EmployeeApp/index.html',context)


def readEmployee(request):
  read = Employee.objects.all()
  context ={'read':read}
  return render(request,'EmployeeApp/read.html',context)

def updateEmployee(request,id):
  add = Employee.objects.get(pk=id)
  form = EmployeeForm(instance=add)
  if request.method == 'POST':
    form = EmployeeForm(request.POST,instance=add)
    if form.is_valid():
      form.save()
      return redirect('home')
  context = {'form':form}
  return render(request,'EmployeeApp/update.html',context)

def deleteEmployee(request,id):
  delEmployee = Employee.objects.get(id=id)
  if request.method == "POST":
    delEmployee.delete()
    return redirect('home')
  context = {'delEmployee':delEmployee}
  return render(request,"EmployeeApp/delete.html",context)

def loginPage(request):
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']

    try:
      user = User.objects.get(username=username)
    except:
      messages.warning(request,'Username does not exit')
    

    user = authenticate(request,username=username,password=password)

    if user is not None:
      login(request,user)
      return redirect('home')
    else:
      messages.warning(request,'Username or password is incorrect')
  return render(request,'EmployeeApp/login.html')


def logoutPage(request):
  logout(request)
  return redirect('login')


def register(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, f'Your account has been created. You can log in now!')    
            return redirect('login')
    

    context = {'form': form}
    return render(request,'EmployeeApp/register.html',context)



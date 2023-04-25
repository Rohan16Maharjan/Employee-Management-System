from django.shortcuts import render,redirect
from .forms import EmployeeForm,RegisterForm,RoleForm,DepartmentForm
from .models import Employee,Department,Role
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
      return redirect('emp')
  context = {'form':form}
  return render(request,'EmployeeApp/addEmp.html',context)



def addRole(request):
  role = RoleForm()
  if request.method == 'POST':
    form = RoleForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('depart')
  context = {'role':role}
  return render(request,'EmployeeApp/addRole.html',context)


def addDepart(request):
  depart = DepartmentForm()
  if request.method == 'POST':
    form = DepartmentForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('depart')
  context = {'depart':depart}
  return render(request,'EmployeeApp/addDepart.html',context)


def readEmployee(request):
  read = Employee.objects.all()
  context ={'read':read}
  return render(request,'EmployeeApp/read.html',context)

def readDepartment(request):
  read = Department.objects.all()
  context ={'read':read}
  return render(request,'EmployeeApp/readDepart.html',context)

def readRole(request):
  read = Role.objects.all()
  context ={'read':read}
  return render(request,'EmployeeApp/readRole.html',context)

def updateEmployee(request,id):
  add = Employee.objects.get(pk=id)
  form = EmployeeForm(instance=add)
  if request.method == 'POST':
    form = EmployeeForm(request.POST,instance=add)
    if form.is_valid():
      form.save()
      return redirect('emp')
  context = {'form':form}
  return render(request,'EmployeeApp/update.html',context)

def deleteEmployee(request,id):
  delEmployee = Employee.objects.get(id=id)
  if request.method == "POST":
    delEmployee.delete()
    return redirect('emp')
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


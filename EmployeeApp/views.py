from django.shortcuts import render,redirect
from .forms import EmployeeForm,RegisterForm,RoleForm,DepartmentForm
from .models import Employee,Department,Role
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import  login,authenticate,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# views.py
from django.contrib.auth.views import (
    PasswordResetView, 
    PasswordResetDoneView, 
    PasswordResetConfirmView, 
    PasswordResetCompleteView
)
from django.urls import reverse_lazy
from .forms import CustomPasswordResetForm

class CustomPasswordResetView(PasswordResetView):
    template_name = 'EmployeeApp/password_reset.html'
    form_class = CustomPasswordResetForm
    success_url = reverse_lazy('password_reset_done')

class CustomPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'EmployeeApp/password_reset_done.html'

class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'EmployeeApp/password_reset_confirm.html'
    success_url = reverse_lazy('password_reset_complete')

class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'EmployeeApp/password_reset_complete.html'


# Create your views here.
@login_required
def home(request):
  return render(request,'EmployeeApp/home.html')
@login_required
def depart(request):
  return render(request,'EmployeeApp/depart.html')
@login_required
def emp(request):
  return render(request,'EmployeeApp/emp.html')
@login_required
def addEmployee(request):
  form = EmployeeForm()
  if request.method == 'POST':
    form = EmployeeForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('emp')
  context = {'form':form}
  return render(request,'EmployeeApp/addEmp.html',context)


@login_required
def addRole(request):
  role = RoleForm()
  if request.method == 'POST':
    form = RoleForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('depart')
  context = {'role':role}
  return render(request,'EmployeeApp/addRole.html',context)

@login_required
def addDepart(request):
  depart = DepartmentForm()
  if request.method == 'POST':
    form = DepartmentForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('depart')
  context = {'depart':depart}
  return render(request,'EmployeeApp/addDepart.html',context)

@login_required
def readEmployee(request):
  read = Employee.objects.all()
  context ={'read':read}
  return render(request,'EmployeeApp/read.html',context)

@login_required
def readDepartment(request):
  read = Department.objects.all()
  context ={'read':read}
  return render(request,'EmployeeApp/readDepart.html',context)

@login_required
def readRole(request):
  read = Role.objects.all()
  context ={'read':read}
  return render(request,'EmployeeApp/readRole.html',context)

@login_required
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

@login_required
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

@login_required
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

# validators.py
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _

def custom_password_validation(password):
    # Implement your custom password validation logic here
    # Return True if the password is valid, otherwise raise a ValidationError
    if len(password) < 8:
        raise ValidationError(_("Your password must contain at least 8 characters."))
    if password.isdigit():
        raise ValidationError(_("Your password can't be entirely numeric."))
    # Add more custom validation rules as needed

    return True

from django.forms import ModelForm
from .models import Employee
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class EmployeeForm(ModelForm):
  first_name = forms.CharField(max_length=101)
  last_name = forms.CharField(max_length=101)
  email = forms.EmailField()
  class Meta:
    model = Employee
    fields = ['first_name','last_name','dept','salary','bonus','Role','phone']






class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=101)
    last_name = forms.CharField(max_length=101)
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','first_name', 'last_name', 'email', 'password1', 'password2']

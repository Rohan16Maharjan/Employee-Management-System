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
    def __init__(self,*args,**kwargs):
      super(RegisterForm,self).__init__(*args,**kwargs)

      for name,field in self.fields.items():
        field.widget.attrs.update({'class':'text email w3lpass'})
    
      self.fields['username'].widget.attrs['placeholder'] = 'UserName'
      self.fields['first_name'].widget.attrs['placeholder'] = 'FirstName'
      self.fields['last_name'].widget.attrs['placeholder'] = 'LastName'
      self.fields['email'].widget.attrs['placeholder'] = 'Email'
      self.fields['password1'].widget.attrs['placeholder'] = 'Password'
      self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'


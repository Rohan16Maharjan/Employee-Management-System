from django.forms import ModelForm
from .models import Employee,Department,Role
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


from django.contrib.auth.forms import PasswordResetForm

class CustomPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))


class EmployeeForm(ModelForm):
    first_name = forms.CharField(max_length=101)
    last_name = forms.CharField(max_length=101)
    
  
    class Meta:
      model = Employee
      fields = ['first_name','last_name','dept','salary','bonus','Role','phone']
      

    def __init__(self,*args,**kwargs):
      super(EmployeeForm,self).__init__(*args,**kwargs)

      for name,field in self.fields.items():
        field.widget.attrs.update({'class':'form-control input-md '})
    



class RoleForm(ModelForm):
    class Meta:
      model = Role
      fields = ['name']
      


    def __init__(self,*args,**kwargs):
      super(RoleForm,self).__init__(*args,**kwargs)

      for name,field in self.fields.items():
        field.widget.attrs.update({'class':'text email w3lpass  '})
      self.fields['name'].widget.attrs['placeholder'] = 'Role'


class DepartmentForm(ModelForm):
    class Meta:
      model = Department
      fields = ['name','location']
      


    def __init__(self,*args,**kwargs):
      super(DepartmentForm,self).__init__(*args,**kwargs)

      for name,field in self.fields.items():
        field.widget.attrs.update({'class':'text email w3lpass '})
      self.fields['name'].widget.attrs['placeholder'] = 'Name'
      self.fields['location'].widget.attrs['placeholder'] = 'Location'





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
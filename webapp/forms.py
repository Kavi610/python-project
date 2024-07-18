from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Record,Student
from django.contrib.auth.forms import AuthenticationForm 
from django.forms.widgets import PasswordInput,TextInput
from django import forms

#register/create a user

class CreateUserForm(UserCreationForm):
    
    class Meta:
        model=User
        fields=["username","password1","password2"]
        
#login a user
class LoginForm(AuthenticationForm):
    username=forms.CharField(widget=TextInput())
    password=forms.CharField(widget=PasswordInput())


#create record
class CreateRecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields=['first_name','last_name','email','phone','address','city','province','country']
        
#update record
class UpdateRecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields=['first_name','last_name','email','phone','address','city','province','country']
        
#upload files
class UploadFileForm(forms.ModelForm):
    class Meta:
        model=Student
        fields=['title','pdf']
    





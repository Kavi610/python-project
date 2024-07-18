from django.db import models
#fuleupload validation
from django.core.validators import FileExtensionValidator
#install python-magic-bin
import magic

# Create your models here.
class Record(models.Model):
    creation_date=models.DateTimeField(auto_now_add=True)
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email=models.CharField(max_length=225)
    phone=models.CharField(max_length=20)
    address=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    province=models.CharField(max_length=100)
    country=models.CharField(max_length=100)
    
    
    def __str__(self):
        return self.first_name+"  "+self.last_name
    
#upload file
class Student(models.Model):
    title=models.CharField(max_length=100,null=True,blank=True)
    pdf=models.FileField(upload_to='books/covers/',null=True,blank=True)
    
    def __str__(self):
        return self.title
    
    


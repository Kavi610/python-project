from django.shortcuts import render,redirect
from .forms import CreateUserForm,LoginForm,CreateRecordForm,UpdateRecordForm,UploadFileForm
#login
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
#dashboard
from django.contrib.auth.decorators import login_required
#model.py
from .models import Record
from django.contrib import messages 
#upload file
from django.http import HttpResponse
from .models import Student
from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage
#install python-magic-bin
#import magic
#from django.http import handle_uploaded_file
#from .models import ModelWithFileField



# Create your views here.
def home(request):
    return render(request,'webapp/index.html')

# -register
def register(request):
    form=CreateUserForm()
    
    if request.method=="POST":
        form=CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Your record  was successfully register!")
            return redirect("login")
            
    context={'form':form}
    return render(request,'webapp/register.html',context=context)
    
    
#Login a user
def my_login(request):
    form=LoginForm()
        
    if request.method == "POST":
        form=LoginForm(request,data=request.POST)
            
        if form.is_valid():
            username=request.POST.get("username")
            password=request.POST.get("password")
                
            user=authenticate(request,username=username,password=password)
            if user is not None:
                auth.login(request,user)
                messages.success(request,"You have logged")
                return redirect("dashboard")
    context={'form':form}
    return render(request,'webapp/my-login.html',context=context)



#dashboard
@login_required(login_url="my-login")
def dashboard(request):
    
    my_records=Record.objects.all()
    context={'records':my_records}
    return render(request,'webapp/dashboard.html',context=context)
                
                
#create a records
@login_required(login_url="my-login")
def create_record(request):
    form=CreateRecordForm()
    if request.method=='POST':
        form=CreateRecordForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Your record was successfully created!")
            return redirect("dashboard")
    context={'form':form}
        
    return render(request,'webapp/create-record.html',context=context)
#Update a  record 
@login_required(login_url="my-login")
def update_record(request,pk):#pk means primary key such as 1,2,3..
    record=Record.objects.get(id=pk)
    form=UpdateRecordForm(instance=record)
    if request.method=='POST':
        form=CreateRecordForm(request.POST,instance=record)
        if form.is_valid():
            form.save()
            messages.success(request,"Your record  was updated!")
            return redirect("dashboard")
    context={'form':form}
        
    return render(request,'webapp/update-record.html',context=context)


#read / view a singular record
@login_required(login_url="my-login")
def singular_record(request,pk):
    all_record=Record.objects.get(id=pk)
    context={'record':all_record}
    return render(request,'webapp/view-record.html',context=context)


#Delete record
@login_required(login_url="my-login")
def delete_record(request,pk):
    record=Record.objects.get(id=pk)
    record.delete()
    messages.success(request,"Your record was successfully deleted!")
    return redirect("dashboard")
                   
                
# user logout

def user_logout(request):
    auth.logout(request)
    messages.success(request,"Logout success!")
    return redirect("login")


#upload files
def uploadfile(request):
    if request.method=="POST":
        #form=UploadFileForm(request.POST,request.FILES)
        file=request.FILES['document']
        #print(file.name)
        #print(file.size)
        fs=FileSystemStorage()
        name=fs.save(file.name,file.size)
        context['url']=fs.url(name)
        
        
        #student=Student.objects.create(filename=file)
        #student.save()
        #return HttpResponse("The Student with id " + str(student.pk) + "has the file : " + str(student.filename))
    #else:
        #form=UploadFileForm()
    #form=UploadFileForm()
    #context={'form':form}
    context={}
    return render(request, "webapp/file-upload.html",context=context)


#Here’s a common way you might handle an uploaded file:
def book_list(request):
    books=Student.objects.all()
    return render(request,"webapp/book_list.html")

def upload_book(request):
    form=UploadFileForm()
    if request.method=="POST":
        form=UploadFileForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,"Your document  was updated!")
            return redirect('book_list')
    context={'form':form}
    return render(request,"webapp/upload_book.html",context=context)
    

        
        



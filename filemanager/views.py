from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import User,Document
import json
# Create your views here.

def index(request):
    if(request.method == "POST"):
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.filter(username=username,password=password).values()[0]
        request.session['user'] = user
        if user:
            return redirect('/home')
    else:
        return render(request,'login.html') 

def register(request):
    if(request.method == "POST"):
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        print(username,email,password)
        User.objects.create(username=username,email=email,password=password)
        return redirect('/')
    else:
        return render(request,'register.html')

def home(request):
    if(request.session['user']):
        return render(request,'home.html')
    else:
        redirect('/')

def specific_docfield(request,document_field):
    if(request.session['user'] and document_field):
        request.session['document_field']=document_field
        documents = Document.objects.filter(field=document_field).values()
        return render(request,'table.html',{'documents':documents})
    else:
        redirect('/')
def addDocument(request):
    if(request.method == "POST"):
        document_name = request.POST['document_name']
        version = request.POST['version']
        desc = request.POST['desc']
        status = request.POST['status']
        file = request.POST['file']
        file = bytes(file,encoding='utf-8')
        field = request.session['document_field']
        Document.objects.create(document_name=document_name,version=version,file=file,desc=desc,status=status,field=field)
        return redirect('/home')
    return render(request,'addDocument.html') 
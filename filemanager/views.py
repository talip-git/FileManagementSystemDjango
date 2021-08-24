from django.db.models import base
from django.shortcuts import render,redirect
from django.http import HttpResponse,FileResponse
from .models import User,Document
from datetime import datetime
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
        User.objects.create(username=username,email=email,password=password)
        return redirect('/')
    else:
        return render(request,'register.html')

def home(request):
    if(request.session.get('user')):

        fields = Document.objects.values('field').distinct().order_by('field')
        alldocuments = Document.objects.values('document_name','field').distinct()

        return render(request,'home.html',{'alldocuments':alldocuments,'fields':fields})
    else:
       return redirect('/')

def specific_docfield(request,document_name):
    if(request.session.get('user') and document_name):

        documents = Document.objects.filter(document_name=document_name)
        document = documents[0]

        fields = Document.objects.values('field').distinct().order_by('field')
        alldocuments = Document.objects.values('document_name','field').distinct()

        return render(request,'table.html',{'alldocuments':alldocuments,'documents':documents,'fields':fields,'document':document})
    else:
        return redirect('/')
def addDocument(request):
    if(request.method == "POST"):
        document_name = request.POST['document_name']
        version = request.POST['version']
        desc = request.POST['desc']
        status = request.POST['status']
        file = request.FILES['file']
        field = request.POST['field']
        doc = Document(document_name=document_name,version=version,file=file,desc=desc,status=status,field=field)
        doc.save()
        return redirect('/home')
    return render(request,'addDocument.html')

#Not working
def download(request,document_name,document_version):
    if(request.session.get('user') and document_name and document_version):
        file = Document.objects.filter(document_name=document_name,version=document_version).values('file')[0]
        file = file['file'].decode('utf-8')
        response = FileResponse(file)
        response['content-type'] = 'application/pdf'
        return response
    else:
        return redirect('/home')

def logout(request):
    request.session.pop('user')
    return redirect('/') 

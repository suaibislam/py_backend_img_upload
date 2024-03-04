from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Student
from .forms import ImageForm
from .models import Image


# Create your views here.
def index(request):
           data = Student.objects.all()
           print(data)
           return render(request,'index_one.html',{'data':data})

def insert(request):
      if request.method=="POST":
           name=request.POST['text']
           print(name)
           database=Student(name=name)
           database.save()
           return redirect("/")
      return render(request,'index_one.html')
        
        
def updateData(request,id):
     if request.method=="POST":
          name=request.POST['text']
          edit = Student.objects.get(id=id)
          edit.name=name
          edit.save()
          return redirect("/")
     d=Student.objects.get(id=id)
     # print(d.name)
     return render(request,'edit.html',{'d':d})
              
def deleteData(request,id):
      d=Student.objects.get(id=id)
      d.delete()
      return redirect("/")
                   
                   
def home(request):
 if request.method == "POST":
  form = ImageForm(request.POST, request.FILES)
  if form.is_valid():
   form.save()
 form = ImageForm()
 img = Image.objects.all()
 return render(request, 'myapp/home.html', {'img':img, 'form':form})                   
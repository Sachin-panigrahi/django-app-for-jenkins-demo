from django.shortcuts import render,redirect
from .models import *
# Create your views here.

def home(request):
    queryset = Tasks.objects.all()
    if request.GET.get('search'):
      data=request.GET.get('search')
      queryset=queryset.filter(name__icontains = data)
        

    return render(request,"home.html",{'queryset':queryset})

def add_task(request):
    if request.method=="POST":
        data = request.POST
        name = data.get("name")
        description = data.get("description")
        status = data.get("status")
        Tasks.objects.create(
            name = name,
            description = description,
            status = status
        )
        return redirect('/')
        
    return render(request,"add-task.html")
    


def delete_task(request,id):

    queryset = Tasks.objects.get(id=id)
    queryset.delete()

    return redirect('/')


def update_task(request,id):
    queryset = Tasks.objects.get(id=id)
    if request.method == "POST":
        data = request.POST
        name = data.get('name')
        description = data.get('description')
        status = data.get('status')

        queryset.name = name
        queryset.description = description
        queryset.status = status
        queryset.save()
        return redirect('/')

    return render(request,"update_task.html",{'queryset':queryset})
        
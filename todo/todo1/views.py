from django.shortcuts import render,redirect
from .models import *

# Create your views here.
def index(request):
    if request.method == "POST":
        data=request.POST
        list_data = data.get("title")
        
        task = Task(title=list_data)
        task.save()
        return redirect("/")
    
    task_info=Task.objects.all()
    
        
        
    return render(request,"index.html",{"task_data":task_info})

def delete(request,id):
    task_data = Task.objects.get(id=id)
    task_data.delete()
    
    return redirect("/")
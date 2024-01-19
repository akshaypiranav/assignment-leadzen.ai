from django.shortcuts import render,redirect
from .models import Todo
from django.contrib import messages
from datetime import datetime
# Create your views here.
def index(request):
    if request.method=="POST":
        todoTitle=request.POST['todo']
        description=request.POST['description']
        print(todoTitle,description)
        try:
            todo=Todo.objects.create(todo=todoTitle,decription=description)
            todo.save()
            messages.success(request,"SUCCESSFULLY ADDED")
            print("DDD")
        except:
            messages.error(request,"INTERNAL SERVER ERROR 500")
            print("err")
    try:
        todo=Todo.objects.all()
    except:
        todo="NO VALUE FOUND"

    return render(request,"index.htm",{"data":todo})
def update(request,id):
    if Todo.objects.filter(id=id).exists():
        todo=Todo.objects.get(id=id)
    else:
        return redirect('/')
        
    if request.method=="POST":
        todo=Todo.objects.get(id=id)

        todo.todo=request.POST['todo']
        todo.decription=request.POST['description']
        todo.date=datetime.now()
        todo.save()
        return redirect('/')

    return render(request,"update.htm",{"data":todo})
        
def delete(request,id):
    if(Todo.objects.filter(id=id).exists()):
        todo=Todo.objects.get(id=id)
        todo.delete()
        messages.success(request,"SUCCESFULLY DELETED")
    else:
        messages.error(request,"INVALID OPERATION")

    
    return redirect('/')
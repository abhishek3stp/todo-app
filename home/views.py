from django.shortcuts import render, redirect
from .models import Task

# Create your views here.
def home (reqest):
    tasks = Task.objects.all()
    context = {'tasks': tasks}
    return render(reqest, 'home/home.html', context)

def createTask(request):
    if request.method == 'POST':
        note = request.POST['note']
        task = Task(note = note)
        task.save()
    
    return redirect('/')

def deleteTask(request, slug):
    task = Task.objects.get(id=slug)
    task.delete()
    return redirect('/')


from django.shortcuts import render,redirect
from .models import Task
from . forms import form
# Create your views here.


def demo(request):
    res = Task.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name','')
        priority = request.POST.get('priority','')
        date = request.POST.get('date', '')

        task = Task(name=name,priority=priority,date=date)
        task.save()
    return render(request,"index.html",{'result':res})

# def detail(request):
#
#     return render(request,"detail.html",)

def delete(request,taskid):
    if request.method == 'POST':
        taskout = Task.objects.get(id=taskid)
        taskout.delete()
        return redirect('/')
    return render(request,"delete.html")


def update(request,id):
    task = Task.objects.get(id=id)
    f = form(request.POST or None,instance=task)

    if f.is_valid():
        f.save()
        return redirect('/')
    return render(request,"edit.html",{'f':f,'task':task})




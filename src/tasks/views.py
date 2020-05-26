from django.shortcuts import render, redirect 
from .models import Task
from .forms import TaskForm
# Create your views here.

def index(request):
	tasks = Task.objects.all()

	form = TaskForm()
	if request.method == 'POST':
		form = TaskForm(request.POST)
		if form.is_valid:
			form.save()
		return redirect('index')
	context = {
		'tasks': tasks,
		'form' : form ,
	}
	return render(request, 'index.html',context)

def update(request, pk):
	task = Task.objects.get(id=pk)
	form = TaskForm(instance=task)
	if request.method == 'POST':
		form = TaskForm(request.POST, instance=task)
		if form.is_valid():
			form.save()
		return redirect('index')
	context = {
		'form':form 
	}
	return render(request, 'update_task.html', context)

def delete(request, pk):
	task = Task.objects.get(id=pk)
	if request.method == 'POST':
		task.delete()
		return redirect('index')

	context = {
		'task': task 
	}
	return render(request, 'delete_confirm.html', context)
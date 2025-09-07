from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Task

# all tasks
def tasks(request):
    context ={
        'title': "ToDo App",
        'todo_list': Task.objects.all()
    }
    return render(request, 'todo/tasks.html', context)

# add task
def add_task(request):
    #Check if the request method is POST
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')

        # Create a new Task object and save it to the database(models.py)
        Task.objects.create(title=title, description=description)

        return redirect(reverse('tasks'))
    context = {'title': "Add Task"}

    return render(request, 'todo/form.html', context)

# details of a task
def details(request, item_id):
    item = Task.objects.get(pk=item_id)
    context = {'item': item,
               'title': "Details"}
    return render(request, 'todo/detail.html', context)


# delete a task
def delete_task(request, item_id):
    item = Task.objects.get(pk=item_id)
    item.delete()
    return redirect(reverse('tasks'))


# do complite task
def complite_task(request, item_id):
    task = Task.objects.get(pk=item_id)
    task.completed = True
    task.save()
    return redirect(reverse('tasks'))
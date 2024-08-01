from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from todoapp.models import Task, Tag


def index(request):
    """View function for the home page of the site."""
    tasks = Task.objects.all()
    num_tasks = Task.objects.count()
    num_tags = Tag.objects.count()

    context = {
        "tasks": tasks,
        "num_tasks": num_tasks,
        "num_tags": num_tags,
    }
    return render(request, "todoapp/index.html", context=context)


class TaskCreateView(generic.CreateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("todoapp:index")


class TaskUpdateView(generic.UpdateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("todoapp:index")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("todoapp:index")

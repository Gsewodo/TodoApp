from django.views.generic import DetailView
from django.views.generic.list import ListView
from django.urls import reverse
from .models import Task
from .models import Developer
from .forms import TaskForm
from django import forms
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin

# Create your views here.


class TaskListView(LoginRequiredMixin,PermissionRequiredMixin,ListView):
    permission_required = 'task.task_management'
    model = Task
    template_name = "task/index.html"
    context_object_name = "tasks"
    def get_context_data(self, **kwargs): 
     context = super(ListView, self).get_context_data(**kwargs) #ListView ? 
     context['form'] = TaskForm 
     return context

class TaskDetailView(DetailView):
    model = Task
    template_name = "task/detail.html"
    context_object_name = "tasks"


def delete(request, id):
     Task.objects.get(id=id).delete()
     return HttpResponseRedirect(reverse('task:index'))


def create(request):
    form = TaskForm(request.POST)
    if form.is_valid():
       Task.objects.create(
           title=form.cleaned_data['title'],
           description=form.cleaned_data['description'],
           assignee = form.cleaned_data['assignee'])
    return HttpResponseRedirect(reverse('task:index'))

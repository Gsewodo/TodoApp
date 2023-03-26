from django.shortcuts import render, get_object_or_404
from django.shortcuts import render
from .models import Developer
from django.urls import reverse
#from .forms import DeveloperForm
from .forms import ShortDeveloperForm
from django.views.generic import DetailView, ListView #ajout 
from django.http import HttpResponse, HttpResponseRedirect 
from task.forms import TaskForm
from django.contrib.auth.mixins import LoginRequiredMixin 


class DevDetailVue(LoginRequiredMixin,DetailView):
 model = Developer
 template_name = 'developer/detail.html'

 def get_context_data(self, **kwargs):

  context = super(DetailView, self).get_context_data(**kwargs)
  form = TaskForm(
    initial={
           'assignee': get_object_or_404(Developer, pk=self.kwargs['pk'])
           })

  form.fields['assignee'].disabled = True

  context['form'] = form

  return context


def create(request):
  form = ShortDeveloperForm(request.POST)
  if form.is_valid():
     Developer.objects.create_user( 
       first_name=form.cleaned_data['first_name'], 
       last_name=form.cleaned_data['last_name'] ,
       username=form.cleaned_data['username']), 
  return HttpResponseRedirect(reverse('developer:index'))

def delete(request,id):
     Developer.objects.get(id=id).delete()
     return HttpResponseRedirect(reverse('developer:index'))

class IndexView(LoginRequiredMixin,ListView): 
  model = Developer 
  template_name = "developer/index.html" 
  context_object_name = 'developers'
  def get_context_data(self, **kwargs):
   context = super(IndexView,self).get_context_data(**kwargs) 
   context['form'] = ShortDeveloperForm
   return context






from django.shortcuts import render
from django.views.generic import ListView
from .models import Task

# ListView für die Anzeige aller Tasks
class TaskListView(ListView):
    model = Task
    context_object_name = 'tasks'

# Create your views here.

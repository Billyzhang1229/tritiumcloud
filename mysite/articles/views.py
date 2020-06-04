from django.shortcuts import render
from django.views.generic import ListView, DetailView
from . import models

# Create your views here.
class PostsListView(ListView):
    model = models.PostsModel
    paginate_by = 10
    queryset = model.objects.all()
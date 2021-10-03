from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, UpdateView
from .models import Recipe

# Create your views here.
class RecipeListView(ListView):
    model = Recipe
    
    
# レシピの作成
class RecipeCreateView(CreateView):
    model = Recipe
    fields = ["title", "content", "description"]
    success_url = "/"
    
class RecipeDetailView(DetailView):
    model = Recipe
    
class RecipeUpdateView(UpdateView):
    model = Recipe
    fields = ["title", "content", "description"]
    success_url = "/"
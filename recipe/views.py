from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import Recipe

# Create your views here.
class RecipeListView(ListView):
    model = Recipe
    
    
# レシピの作成
class RecipeCreateView(CreateView):
    model = Recipe
    fields = ["title", "content", "description"]
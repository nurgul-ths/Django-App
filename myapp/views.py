from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList, Item
# Create your views here.

def index(response):
    return HttpResponse("<h1>hello!</h1>")

def test1(response, id):
    ls = ToDoList.objects.get(id=id)
    return render(response, "main/base.html", {"name":ls.name})

def home(response):
    return render(response, "main/home.html", {"name":"test"})

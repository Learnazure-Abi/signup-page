from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def homepage(request):
    return HttpResponse("<h1 style= text-align:center>HelloWorld, homePage for practice application</h1>")

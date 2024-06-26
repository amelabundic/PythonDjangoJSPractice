from django.http import HttpResponse # type: ignore
from django.shortcuts import render # type: ignore

# Create your views here.
def index(request):
    return render(request, "hello/index.html")

def brian(request):
    return HttpResponse("Hello,Brian!")

def david(request):
    return HttpResponse("Hello, David")

def greet(request, name):
    return render(request, "hello/greet.html", {
        "name": name.capitalize()
    })
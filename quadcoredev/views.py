from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
##def index(response):
## return HttpResponse("HELLO!")

def index(response):
    return render(response, "quadcoredev/base.html")


def index(response):
    return render(response, "quadcoredev/index.html")


def act(response):
    return render(response, "quadcoredev/acts.html")

def act1(response):
    return render(response, "quadcoredev/aone.html")

def act2(response):
    return render(response, "quadcoredev/atwo.html")

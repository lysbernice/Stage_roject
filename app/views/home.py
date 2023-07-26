from django.shortcuts import redirect, render
from django.http import HttpRequest

def index(request):
    return render(
        request,
        'app/home/index.html'
        )
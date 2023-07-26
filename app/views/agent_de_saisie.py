from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.contrib import messages

from app.models import Etudiant,Section,Cours,Laureat

def index(request):
    assert isinstance(request, HttpRequest)
    etudiants = Etudiant.objects.all().count()
    sections = Section.objects.all().count()
    cours = Cours.objects.all().count()
    laureats = Laureat.objects.all().count()
    return render(
        request,
        'app/agent_de_saisie/home/index.html',
        {
            'etudiants': etudiants,
            'sections': sections,
            'cours': cours,
            'laureats': laureats
        }
    )
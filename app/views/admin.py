from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.contrib import messages

from app.models import User

def index(request):
    assert isinstance(request, HttpRequest)
    admins = User.objects.filter(role="administrateur").count()
    agent_de_saisie = User.objects.filter(role="agent_de_saisie").count()
    organisateurs = User.objects.filter(role="organisateur").count()
    receptionistes = User.objects.filter(role="récéptioniste").count()
    
    masculins = User.objects.filter(genre='masculin').count()
    feminins = User.objects.filter(genre='feminin').count()
    return render(
        request,
        'app/admin/home/index.html',
        {
            'admins': admins,
            'agent_de_saisie': agent_de_saisie,
            'organisateurs': organisateurs,
            'receptionistes': receptionistes,
           
            'masculins' : masculins,
            'feminins' : feminins
        }
    )
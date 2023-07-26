from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.contrib import messages


from app.models import Laureat
from app.forms import LaureatForm


def index(request):
    assert isinstance(request, HttpRequest)
    laureats= Laureat.objects.all()
    return render(
        request,
        'app/agent_de_saisie/templates/laureats/index.html',
        {
            'laureats': laureats
        }
    )
    
def add(request):
    if request.method == 'GET' :
        form = LaureatForm()
        
    return render(
        request, 
        'app/agent_de_saisie/templates/laureats/add.html',
        {
            'form': form
        }
    )
    
def store(request):
    if request.method == 'POST':
        form = LaureatForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Le laureat' a été enregistré avec succès !")
        else :
            messages.success(request, form.errors)
        return redirect('/agent_de_saisie/templates/laureats')
    
def update(request, id):
    if request.method == 'POST':
        if id == 0:
            form = LaureatForm(request.POST)
        else:
            category = Laureat.objects.get(pk=id)
            form = LaureatForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
        messages.success(request, "Le laureat' a été modifié avec succès !")
        return redirect('/agent_de_saisie/templates/laureats')

def edit(request, id):
    assert isinstance(request, HttpRequest)
    if request.method == 'GET':
        if id == 0:
            form = LaureatForm()
        else:
            laureat = Laureat.objects.get(pk=id)
            form = LaureatForm(instance=laureat)
        return render(
            request,
            'app/agent_de_saisie/templates/laureats/edit.html',
            {
                'form': form,
            }
        )

def delete(request, id):
    laureat = Laureat.objects.get(pk=id)
    laureat.delete()
    messages.success(request, "le laureat a été supprimé avec succès !")
    return redirect('/agent_de_saisie/templates/laureats')


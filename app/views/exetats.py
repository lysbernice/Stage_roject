from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.contrib import messages


from app.models import Exetat
from app.forms import ExetatForm


def index(request):
    assert isinstance(request, HttpRequest)
    exetats = Exetat.objects.all()
    return render(
        request,
        'app/organisateur/templates/exetats/index.html',
        {
            'exetats': exetats
        }
    )
    
def add(request):
    if request.method == 'GET' :
        form = ExetatForm()
        
    return render(
        request, 
        'app/organisateur/templates/exetats/add.html',
        {
            'form': form
        }
    )
    
def store(request):
    if request.method == 'POST':
        form = ExetatForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "L'Edition' a été enregistrée avec succès !")
        else :
            messages.success(request, form.errors)
        return redirect('/organisateur/templates/exetats')
    
def update(request, id):
    if request.method == 'POST':
        if id == 0:
            form = ExetatForm(request.POST)
        else:
            category = Exetat.objects.get(pk=id)
            form = ExetatForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
        messages.success(request, "La commune a été modifiée avec succès !")
        return redirect('/organisateur/templates/exetats')

def edit(request, id):
    assert isinstance(request, HttpRequest)
    if request.method == 'GET':
        if id == 0:
            form = ExetatForm()
        else:
            exetat = Exetat.objects.get(pk=id)
            form = ExetatForm(instance=exetat)
        return render(
            request,
            'app/organisateur/templates/exetats/edit.html',
            {
                'form': form,
            }
        )

def delete(request, id):
    exetat = Exetat.objects.get(pk=id)
    exetat.delete()
    messages.success(request, "L'Edition a été supprimée avec succès !")
    return redirect('/organisateur/templates/exetats')


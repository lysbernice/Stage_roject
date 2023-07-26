from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.contrib import messages


from app.models import Etudiant
from app.forms import EtudiantForm


def index(request):
    assert isinstance(request, HttpRequest)
    etudiants = Etudiant.objects.all()
    return render(
        request,
        'app/agent_de_saisie/templates/etudiants/index.html',
        {
            'etudiants': etudiants
        }
    )
    
def add(request):
    if request.method == 'GET' :
        form = EtudiantForm()
        
    return render(
        request, 
        'app/agent_de_saisie/templates/etudiants/add.html',
        {
            'form': form
            
        }
    )
    
def store(request):
    if request.method == 'POST':
        form = EtudiantForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "L'etudiant' a été enregistré avec succès !")
        else :
            messages.success(request, form.errors)
        return redirect('/agent_de_saisie/templates/etudiants')
    
def update(request, id):
    if id == 0:
        form = EtudiantForm(request.POST)
    else:
        category = Etudiant.objects.get(pk=id)
        form = EtudiantForm(request.POST, instance=category)
    if form.is_valid():
        form.save()
    messages.success(request, "L'etudiant' a été modifié avec succès !")
    return redirect('/agent_de_saisie/templates/etudiants')

def edit(request, id):
    assert isinstance(request, HttpRequest)
    if request.method == 'GET':
        if id == 0:
            form = EtudiantForm()
        else:
            etudiant = Etudiant.objects.get(pk=id)
            form = EtudiantForm(instance=etudiant)
        return render(
            request,
            'app/agent_de_saisie/templates/etudiants/edit.html',
            {
                'form': form,
            }
        )

def delete(request, id):
    etudiant = Etudiant.objects.get(pk=id)
    etudiant.delete()
    messages.success(request, "L'etudiant a été supprimé avec succès !")
    return redirect('/agent_de_saisie/templates/etudiants')


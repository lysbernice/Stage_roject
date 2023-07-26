from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.contrib import messages


from app.models import Cours
from app.forms import CoursForm


def index(request):
    assert isinstance(request, HttpRequest)
    cours = Cours.objects.all()
    return render(
        request,
        'app/agent_de_saisie/templates/cours/index.html',
        {
            'cours': cours
        }
    )
    
def add(request):
    if request.method == 'GET' :
        form = CoursForm()
        
    return render(
        request, 
        'app/agent_de_saisie/templates/cours/add.html',
        {
            'form': form
        }
    )
    
def store(request):
    if request.method == 'POST':
        form = CoursForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Le cours a été enregistré avec succès !")
        else :
            messages.success(request, form.errors)
        return redirect('/agent_de_saisie/templates/cours')
    
def update(request, id):
    if request.method == 'POST':
        if id == 0:
            form = CoursForm(request.POST)
        else:
            category = Cours.objects.get(pk=id)
            form = CoursForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
        messages.success(request, "Le cours a été modifié avec succès !")
        return redirect('/agent_de_saisie/templates/cours')

def edit(request, id):
    assert isinstance(request, HttpRequest)
    if request.method == 'GET':
        if id == 0:
            form = CoursForm()
        else:
            cours = Cours.objects.get(pk=id)
            form = CoursForm(instance=cours)
        return render(
            request,
            'app/agent_de_saisie/templates/cours/edit.html',
            {
                'form': form,
            }
        )

def delete(request, id):
    cours = Cours.objects.get(pk=id)
    cours.delete()
    messages.success(request, "Le cours a été supprimé avec succès !")
    return redirect('/agent_de_saisie/templates/cours')


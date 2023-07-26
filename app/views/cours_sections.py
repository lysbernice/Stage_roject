from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.contrib import messages


from app.models import Section_cours
from app.forms import CoursSectionForm


def index(request):
    assert isinstance(request, HttpRequest)
    cours_sections = Section_cours.objects.all()
    return render(
        request,
        'app/agent_de_saisie/templates/cours_sections/index.html',
        {
            'cours_sections': cours_sections
        }
    )
    
def add(request):
    if request.method == 'GET' :
        form = CoursSectionForm()
        
    return render(
        request, 
        'app/agent_de_saisie/templates/cours_sections/add.html',
        {
            'form': form
        }
    )
    
def store(request):
    if request.method == 'POST':
        form = CoursSectionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "La section a été enregistré avec succès !")
        else :
            messages.success(request, form.errors)
        return redirect('/agent_de_saisie/templates/cours_sections')
    
def update(request, id):
    if request.method == 'POST':
        if id == 0:
            form = CoursSectionForm(request.POST)
        else:
            category = Section_cours.objects.get(pk=id)
            form = CoursSectionForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
        messages.success(request, "La section a été modifié avec succès !")
        return redirect('/agent_de_saisie/templates/cours_sections')

def edit(request, id):
    assert isinstance(request, HttpRequest)
    if request.method == 'GET':
        if id == 0:
            form = CoursSectionForm()
        else:
            section = Section_cours.objects.get(pk=id)
            form = CoursSectionForm(instance=section)
        return render(
            request,
            'app/agent_de_saisie/templates/cours_sections/edit.html',
            {
                'form': form,
            }
        )

def delete(request, id):
    section = Section_cours.objects.get(pk=id)
    section.delete()
    messages.success(request, "L section a été supprimé avec succès !")
    return redirect('/agent_de_saisie/templates/cours_sections')


from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.contrib import messages


from app.models import Section
from app.forms import SectionForm


def index(request):
    assert isinstance(request, HttpRequest)
    sections = Section.objects.all()
    return render(
        request,
        'app/agent_de_saisie/templates/sections/index.html',
        {
            'sections': sections
        }
    )
    
def add(request):
    if request.method == 'GET' :
        form = SectionForm()
        
    return render(
        request, 
        'app/agent_de_saisie/templates/sections/add.html',
        {
            'form': form
        }
    )
    
def store(request):
    if request.method == 'POST':
        form = SectionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "La section a été enregistré avec succès !")
        else :
            messages.success(request, form.errors)
        return redirect('/agent_de_saisie/templates/sections')
    
def update(request, id):
    if request.method == 'POST':
        if id == 0:
            form = SectionForm(request.POST)
        else:
            category = Section.objects.get(pk=id)
            form = SectionForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
        messages.success(request, "La section a été modifié avec succès !")
        return redirect('/agent_de_saisie/templates/sections')

def edit(request, id):
    assert isinstance(request, HttpRequest)
    if request.method == 'GET':
        if id == 0:
            form = SectionForm()
        else:
            section = Section.objects.get(pk=id)
            form = SectionForm(instance=section)
        return render(
            request,
            'app/agent_de_saisie/templates/sections/edit.html',
            {
                'form': form,
            }
        )

def delete(request, id):
    section = Section.objects.get(pk=id)
    section.delete()
    messages.success(request, "L section a été supprimé avec succès !")
    return redirect('/agent_de_saisie/templates/sections')


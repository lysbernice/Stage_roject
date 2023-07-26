from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.contrib import messages

from app.models import Province
from app.forms import ProvinceForm

def index(request):
    assert isinstance(request, HttpRequest)
    provinces = Province.objects.all()
    return render(
        request,
        'app/admin/templates/provinces/index.html',
        {
            'provinces': provinces
        }
    )
    
def add(request):
    if request.method == 'GET' :
        form = ProvinceForm()
        
    return render(
        request, 
        'app/admin/templates/provinces/add.html',
        {
            'form': form
        }
    )
    
def store(request):
    if request.method == 'POST':
        form = ProvinceForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "La province a été enregistrée avec succès !")
        else :
            messages.success(request, form.errors)
        return redirect('/admin/templates/provinces')

def update(request, id):
    if request.method == 'POST':
        if id == 0:
            form = ProvinceForm(request.POST)
        else:
            category = Province.objects.get(pk=id)
            form = ProvinceForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
        messages.success(request, "La province a été modifiée avec succès !")
        return redirect('/admin/templates/provinces')

def edit(request, id):
    assert isinstance(request, HttpRequest)
    if request.method == 'GET':
        if id == 0:
            form = ProvinceForm()
        else:
            province = Province.objects.get(pk=id)
            form = ProvinceForm(instance=province)
        return render(
            request,
            'app/admin/templates/provinces/edit.html',
            {
                'form': form,
            }
        )


def delete(request, id):
    province = Province.objects.get(pk=id)
    province.delete()
    messages.success(request, "La province a été supprimée avec succès !")
    return redirect('/admin/templates/provinces')
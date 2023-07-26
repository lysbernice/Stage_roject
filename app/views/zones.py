from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.contrib import messages


from app.models import Zone, Province, Commune
from app.forms import ZoneForm


def index(request):
    assert isinstance(request, HttpRequest)
    zones = Zone.objects.all()
    return render(
        request,
        'app/admin/templates/zones/index.html',
        {
            'zones': zones
        }
    )
    
def add(request):
    if request.method == 'GET' :
        form = ZoneForm()
        provinces = Province.objects.all()
    return render(
        request, 
        'app/admin/templates/zones/add.html',
        {
            'form': form,
            'provinces': provinces
        }
    )
    
def store(request):
    if request.method == 'POST':
        form = ZoneForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "La zone a été enregistrée avec succès !")
        else :
            messages.success(request, form.errors)
        return redirect('/admin/templates/zones')
    
def update(request, id):
    if request.method == 'POST':
        if id == 0:
            form = ZoneForm(request.POST)
        else:
            category = Zone.objects.get(pk=id)
            form = ZoneForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
        messages.success(request, "La zone a été modifiée avec succès !")
        return redirect('/admin/templates/zones')

def edit(request, id):
    assert isinstance(request, HttpRequest)
    if request.method == 'GET':
        if id == 0:
            form = ZoneForm()
        else:
            zone = Zone.objects.get(pk=id)
            form = ZoneForm(instance=zone)
        return render(
            request,
            'app/admin/templates/zones/edit.html',
            {
                'form': form,
            }
        )


def delete(request, id):
    province = Zone.objects.get(pk=id)
    province.delete()
    messages.success(request, "La zone a été supprimée avec succès !")
    return redirect('/admin/templates/zones')

def getCommunes(request):
    province_id = request.GET.get('province_id')
    communes = Commune.objects.filter(province_id = province_id).order_by('nom')
    return render(
        request,
        'app/admin/templates/zones/getCommunes.html',
        {
            'communes':communes
        }
    )
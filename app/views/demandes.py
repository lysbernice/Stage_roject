from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.contrib import messages


from app.models import Rendez_vous
from app.forms import Rendez_vousForm


def index(request):
    assert isinstance(request, HttpRequest)
    demandes = Rendez_vous.objects.all()
    return render(
        request,
        'app/receptioniste/templates/demandes/index.html',
        {
            'demandes': demandes
        }
    )
    
def add(request):
    if request.method == 'GET' :
        form = Rendez_vousForm()
        
    return render(
        request, 
        'app/receptioniste/templates/demandes/add.html',
        {
            'form': form
            
        }
    )
    

    
# def store(request):
#     if request.method == 'POST':
#         form = Rendez_vousForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, "Votre demande a été envoyée avec succès !")
#         else :
#             messages.success(request, form.errors)
#         return redirect('/receptioniste/templates/demandes')
    
def update(request, id):
    if request.method == 'POST':
        if id == 0:
            form = Rendez_vousForm(request.POST)
        else:
            category = Rendez_vous.objects.get(pk=id)
            form = Rendez_vousForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
        messages.success(request, "Votre demande a été modifiée avec succès !")
        return redirect('/receptioniste/templates/demandes')

def edit(request, id):
    assert isinstance(request, HttpRequest)
    if request.method == 'GET':
        if id == 0:
            form = Rendez_vousForm()
        else:
            rendez_vous = Rendez_vous.objects.get(pk=id)
            form = Rendez_vousForm(instance=rendez_vous)
        return render(
            request,
            'app/receptioniste/templates/demandes/add.html',
            {
                'form': form,
            }
        )

def delete(request, id):
    rendez_vous = Rendez_vous.objects.get(pk=id)
    rendez_vous.delete()
    messages.success(request, "Votre demande a été supprimé avec succès !")
    return redirect('/receptioniste/templates/demandes')


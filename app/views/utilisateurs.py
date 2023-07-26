from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.contrib import messages
from app.models import User, Province, Commune, Zone
from app.forms import UtilisateurForm, UserEditForm
from django.contrib.auth.hashers import make_password, check_password

from django.contrib.auth import authenticate, login, logout


def index(request):
    assert isinstance(request, HttpRequest)
    users = User.objects.all()
    return render(
        request,
        'app/admin/templates/utilisateurs/index.html',
        {
            'users': users
        }
    )
    
def add(request):
    if request.method == 'GET' :
        form = UtilisateurForm()
        provinces = Province.objects.all()
        communes = Commune.objects.all()
    return render(
        request, 
        'app/admin/templates/utilisateurs/add.html',
        {
            'form': form,
            'provinces': provinces,
            'communes' : communes
        }
    )
    
def store(request):
    if request.method == 'POST':
        form = UtilisateurForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "L' Utilisateur a été enregistrée avec succès !")
        else :
            messages.success(request, form.errors)
        return redirect('/admin/templates/utilisateurs')
    
def update(request, id):
    if request.method == 'POST':
        if id == 0:
            form = UserEditForm(request.POST)
        else:
            category = User.objects.get(pk=id)
            form = UserEditForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
        messages.success(request, "L' Utilisateur' a été modifiée avec succès !")
        return redirect('/admin/templates/utilisateurs')

def edit(request, id):
    assert isinstance(request, HttpRequest)
    if request.method == 'GET':
        if id == 0:
            form = UtilisateurForm()
        else:
            user = User.objects.get(pk=id)
            form = UtilisateurForm(instance=user)
        return render(
            request,
            'app/admin/templates/utilisateurs/edit.html',
            {
                'form': form,
            }
        )


def delete(request, id):
    user = User.objects.get(pk=id)
    user.delete()
    messages.success(request, "L'Utilisateur' a été supprimée avec succès !")
    return redirect('/admin/templates/utilisateurs')


def getCommunes(request):
    province_id = request.GET.get('province_id')
    communes = Commune.objects.filter(province_id = province_id).order_by('nom')
    return render(
        request,
        'app/admin/templates/utilisateurs/getCommunes.html',
        {
            'communes':communes
        }
    )
    
def getZones(request):
    page_title = 'Get Zone'
    commune_id = request.GET.get('commune_id')
    zones = Zone.objects.filter(commune_id = commune_id).order_by('nom')
    return render(
        request,
        'app/admin/templates/utilisateurs/getZones.html',
        {
            'zones': zones
        }
    )   


# def user_login(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
        
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             if user.role == 'administrateur':
#                 return redirect('/admin/home')
#             elif user.role == 'organisateur':
#                 return redirect('/organisateur/home')
#             elif user.role == 'agent_de_saisie':
#                 return redirect('/agent_de_saisie/home')
#             elif user.role == 'receptioniste':
#                 return redirect('/home')     
#         else:
#             messages.info(request, 'Username or password incorrect')   
#     return render(
#         request,
#         'app/admin/templates/utilisateurs/login.html'
#     )

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password = password)
        
        if user is not None:
            login(request, user)
            # Rediriger vers la page d'accueil de l'utilisateur approprié en fonction de son rôle
            if user.role == 'administrateur':
                return redirect('/')
            elif user.role == 'organisateur':
                return redirect('/organisateur/home')
            elif user.role == 'agent_de_saisie':
                return redirect('/agent_de_saisie/home')
            elif user.role == 'receptioniste':
                return redirect('/receptioniste/home') 
        else:
            # Si l'authentification échoue, rediriger vers la page de connexion avec un message d'erreur
            return render(
                request, 
                'app/admin/templates/utilisateurs/login.html', {'error': 'Nom d\'utilisateur ou mot de passe incorrect.'})
    return render(
         request,
         'app/admin/templates/utilisateurs/login.html'
     )
    
def user_logout(request):
    logout(request)
    return redirect('/login')
from django.http import HttpRequest
from django.shortcuts import render
from django.contrib import messages
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from datetime import datetime, timedelta
from app.models import Rendez_vous
import qrcode


from app.forms import Rendez_vousForm
from .mailsend import EmailConfirmation


def index(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/public/home/index.html',
        {      
               
        }
    ) 
#formulaire add
def add_formulaire(request):
    if request.method == 'GET' :
        form = Rendez_vousForm()
    return render(
        request, 
        'app/public/formulaire/formulaire.html',
        {
            'form':form
        }
    )
def store(request):
    if request.method == 'POST':
        form = Rendez_vousForm(request.POST)
        if form.is_valid():
            nom = form['nom'].value()
            prenom = form['prenom'].value()
            email = form['email'].value()
            gender = form['gender'].value()
            code_centre = form['code_centre'].value()
            code_participation = form['code_participation'].value()
            code_ecole = form['code_ecole'].value()
            type_documents = form['type_documents'].value()
            edition = form['edition'].value()
            date_delivrance = datetime.now().date() + timedelta(days=14)
            rdv=Rendez_vous.objects.create(nom=nom, prenom=prenom, email=email, gender=gender, code_centre=code_centre, code_participation=code_participation, code_ecole=code_ecole,type_documents=type_documents,edition=edition, date_delivrance=date_delivrance)
            rdv.save()
            mail=form.cleaned_data['email']
            messages.success(request, "Votre demande a été envoyée avec succès !")
            EmailConfirmation(request, email)
            return render(
                request,
                'app/public/formulaire/confirmation.html'
            )
        else :
            messages.error(request, form.errors)
            return render(request, 'app/public/formulaire/formulaire.html', {'form': form})
        # return redirect('/public/formulaire')
        
#fonction pour renvoyer un mail a l'etudiant

from django.forms import ModelForm
from app.models import Etudiant

class EtudiantForm(ModelForm):
    class Meta:
        model = Etudiant
        fields = '__all__'
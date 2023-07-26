from django.forms import ModelForm
from app.models import Rendez_vous

class Rendez_vousForm(ModelForm):
    class Meta:
        model = Rendez_vous
        fields = '__all__'
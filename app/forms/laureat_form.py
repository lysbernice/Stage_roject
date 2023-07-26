from django.forms import ModelForm
from app.models import Laureat

class LaureatForm(ModelForm):
    class Meta:
        model = Laureat
        fields = '__all__'
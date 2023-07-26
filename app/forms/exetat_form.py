from django.forms import ModelForm
from app.models import Exetat

class ExetatForm(ModelForm):
    class Meta:
        model = Exetat
        fields = '__all__'
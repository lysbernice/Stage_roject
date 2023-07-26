from django.forms import ModelForm
from app.models import Cours


class CoursForm(ModelForm):
    class Meta:
        model = Cours
        fields = '__all__'
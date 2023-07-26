from django.forms import ModelForm
from app.models import Section_cours


class CoursSectionForm(ModelForm):
    class Meta:
        model = Section_cours
        fields = '__all__'
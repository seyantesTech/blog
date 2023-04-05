from django.forms import ModelForm
from .models import Projet

class ProjetForm(ModelForm):
    class Meta:
        model = Projet
        fields = ['titre', 'contenu', 'slug', 'image']

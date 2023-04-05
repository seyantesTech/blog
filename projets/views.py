from django.shortcuts import render, get_object_or_404
from .models import Projet

# from django.urls import reverse

def projets_view(request):
    projets = Projet.objects.all().order_by('-date_publication')
    return render(request, 'projets/list.html', context={"projets":projets})
"""
le parametre 'context' sert à projet.html 
d'acceder à nos projets, qui sont en base, dans notre fichier html
le procédé va passer par des tags de template 
"""

def projet_view(request, slug):
    projet = get_object_or_404(Projet, slug=slug)
    return render(request, 'projets/detail.html', context={'projet': projet})


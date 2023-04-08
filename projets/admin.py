from django.contrib import admin
from .models import Projet
# from django.contrib.auth.models import User

# https://docs.djangoproject.com/fr/4.1/topics/auth/default/
# https://docs.djangoproject.com/fr/4.1/ref/contrib/auth/#django.contrib.auth.models.UserManager.create_user
# https://www.youtube.com/shorts/Is9MXXTV9tc

class AdminProjet(admin.ModelAdmin):
    list_display = ('titre','slug','contenu','date_publication')

admin.site.register(Projet,AdminProjet) 






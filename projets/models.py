from django.db import models

class Projet(models.Model):
    # https://docs.djangoproject.com/fr/4.1/ref/models/fields/#field-types
    titre = models.CharField(max_length=150)
    slug = models.SlugField(max_length=100)
    contenu = models.TextField()
    date_publication = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(default='default.jpg')

    class Meta:
        verbose_name = ('Projet')
        verbose_name_plural = ('Projets')


    #si on veut afficher les objets de manière plus décrite 
    def __str__(self):
        return self.titre
    

    
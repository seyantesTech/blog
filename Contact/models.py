from django.db import models

class Contact(models.Model):
    nom = models.CharField(max_length=250)
    Prenom = models.CharField(max_length=250)
    Email = models.EmailField()
    phone = models.CharField(max_length=10)
    message = models.TextField(max_length=3000)

    def __str__(self):
        return self.email

from django.contrib import admin
from django.urls import path
from . import views

app_name = "projets"

urlpatterns = [
    path('',views.projets_view, name='projets'),
    path('<slug:slug>/',views.projet_view, name='projet'),
]

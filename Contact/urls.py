from django.urls import path
from Contact import views

app_name = 'contact'

urlpatterns = [
    path('', views.contact, name="contact"),   
]
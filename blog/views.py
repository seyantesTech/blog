from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.core.mail import send_mail

def home_view(request):
    return render(request, 'home.html')



def remerciements_view(request):
    return HttpResponse('Merci de nous avoir contacté')


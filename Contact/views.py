from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import Contact
from .forms import ContactForm

# Create your views here.

def contact(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            nom = form.cleaned_data['nom']
            prenom = form.cleaned_data['prenom']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

        contact_data = Contact(nom=nom, Prenom=prenom, Email=email, message=message)
        contact_data.save()
        return render(request, 'contact/success.html')
    return render(request, 'contact/contact.html', {"form":form})


#     form = ContactForm()
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#         #    print(form.cleaned_data)
#             nom = form.cleaned_data['nom']
#             prenom = form.cleaned_data['prenom']
#             email = form.cleaned_data['email']
#             message = form.cleaned_data['message']
from django.shortcuts import render, HttpResponse
from .models import contact
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'myapp/index.html')

def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        dec = request.POST.get('dec') 
        con = contact(name = name, email = email , phone = phone, dec = dec)
        con.save()
        messages.success(request, 'Your message has been sent')

    return render(request, 'myapp/contacts.html')

def about(request):
    return render(request, 'myapp/about.html')

def services(request):
    return render(request, 'myapp/services.html')
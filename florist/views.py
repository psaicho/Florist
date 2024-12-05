from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import Contact


def home(request):
    return render(request, 'home.html')


def contact(request):
    if request.method == 'POST':
        form = Contact(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            message = form.cleaned_data['message']
            phone = form.cleaned_data['phone']
            email = form.cleaned_data['email']
            # Tutaj należy dodać zapis do bazy danych
            return render(request, 'contact.html', {'method': 'POST'})
    else:
        form = Contact()

    return render(request, 'contact.html', {'form': form, 'method': 'GET'})


def products(request):
    return render(request, 'products.html')

def about(request):
    return render(request, 'about.html')

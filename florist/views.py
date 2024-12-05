from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import ContactForms


def home(request):
    return render(request, 'home.html')



def contact(request):
    if request.method == 'GET':
        form = ContactForms(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            message = form.cleaned_data['message']
            phone = form.cleaned_data['phone']
            emaile = form.cleaned_data['email']
            return render(request, 'thank_you.html')
    else:
        form = ContactForms()
    return render(request, 'contact.html', {'form': form, 'method': request.method})

    if request.method == 'POST':
        return render(request, 'contact.html', {'method': request.method})

def products(request):
    return render(request, 'products.html')

def about(request):
    return render(request, 'about.html')

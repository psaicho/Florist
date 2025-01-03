from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import ContactForms
from. import models
from .models import Product
from decimal import Decimal


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForms(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            message = form.cleaned_data['message']
            phone = form.cleaned_data['phone']
            email = form.cleaned_data['email']
            models.Contact.objects.create(
                first_name=first_name,
                last_name=last_name,
                message=message,
                phone=phone,
                email=email
            )
            return render(request, 'contact.html', {'method': 'POST'})
    else:
        form = ContactForms()

    return render(request, 'contact.html', {'form': form, 'method': 'GET'})


def products(request):
    single_flowers = Product.objects.filter(category=1, available=True)
    compositions = Product.objects.filter(category=2, available=True)

    if request.method == 'POST':
        selected_items = []
        total_price = Decimal('0.00')

        for key, value in request.POST.items():
            if key.startswith('quantity_') and value:
                product_id = key.replace('quantity_', '')
                if request.POST.get(f'select_{product_id}'):
                    product = Product.objects.get(id=product_id)
                    quantity = int(value)
                    item_total = product.price * quantity
                    total_price += item_total
                    selected_items.append({
                        'name': product.name,
                        'price': product.price,
                        'quantity': quantity,
                        'total': item_total
                    })

        context = {
            'single_flowers': single_flowers,
            'compositions': compositions,
            'selected_items': selected_items,
            'total_price': total_price
        }
    else:
        context = {
            'single_flowers': single_flowers,
            'compositions': compositions,
            'selected_items': [],
            'total_price': Decimal('0.00')
        }

    return render(request, 'products.html', context)

def about(request):
    return render(request, 'about.html')




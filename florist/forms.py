from django import forms

class ContactForms(forms.Form):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    message = forms.CharField(max_length=1000)
    phone = forms.CharField(max_length=10)
    email = forms.CharField(max_length=100)

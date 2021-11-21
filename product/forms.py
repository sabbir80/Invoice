from django.forms import ModelForm
from .models import Product
from django import forms

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name','code','selling_price']

        widgets ={
            'name':forms.TextInput(attrs={'class': 'form-control', 'id': 'name', 'type': 'text'}),
            'code':forms.TextInput(attrs={'class': 'form-control', 'id': 'code', 'type': 'text'}),
            'selling_price':forms.TextInput(attrs={'class': 'form-control', 'id': 'price', 'type': 'text'}),
        }

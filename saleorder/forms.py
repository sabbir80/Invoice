from django import forms
from product.models import Product
from .models import SaleInvoice
class SaleInvoiceForm(forms.Form):
    invoice = forms.ModelChoiceField(queryset=SaleInvoice.objects.all(),label="Invoice")
    product = forms.ModelChoiceField(queryset=Product.objects.all(), label='Product')
    quantity = forms.IntegerField(label='Quantity')

class NewSaleInvoice(forms.Form):
    invoice_number = forms.CharField(max_length=200, label='Invoice')
    invoice_date = forms.DateField(label='Invoice Date',widget=forms.TextInput(attrs={'class': 'form-control', 'type':'date'}))
    customer_name = forms.CharField(max_length=200, label='Customer')
    product = forms.ModelChoiceField(queryset=Product.objects.all(), label='Product')
    quantity = forms.IntegerField(label='Quantity')
from django import forms
from product.models import Product
class SaleInvoiceForm(forms.Form):
    invoice_number = forms.CharField(max_length=200, label='Invoice')
    invoice_date = forms.DateField(label='Invoice Date')
    customer_name = forms.CharField(max_length=200, label='Customer')
    product = forms.ModelChoiceField(queryset=Product.objects.all(), label='Product')
    quantity = forms.IntegerField(label='Quantity')


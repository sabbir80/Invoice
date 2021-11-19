from django.shortcuts import render
import django
from .forms import SaleInvoiceForm
from .models import *
# Create your views here.
def index(request,**kwargs):
    pass
def add(request,**kwargs):
    context={}
    sale_order = SaleInvoiceForm()
    context['form']=sale_order
    if request.POST:
        data = SaleInvoiceForm(request.POST)
        if data.is_valid():
            print(data.cleaned_data['invoice_number'])
            sale_invoice_obj = SaleInvoice.objects.create()
            sale_invoice_obj.invoice_number = data.cleaned_data['invoice_number']
            sale_invoice_obj.customer_name = data.customer_name
            sale_invoice_obj.invoice_date = data.invoice_date
            sale_invoice_details_obj = SaleInvoiceDetails.objects.create()
            sale_invoice_details_obj.product_id = data.product
            sale_invoice_details_obj.product_name = data.product.name
            sale_invoice_details_obj.sale_invoice_id = sale_invoice_obj
            sale_invoice_details_obj.quantity = data.quantity
            sale_invoice_details_obj.amount = int(data.quantity*data.product.selling_price)
            sale_invoice_obj.save()
            sale_invoice_details_obj.save()

    return render(request,'sale_invoice.html',context)
def edit(request,**kwargs):
    pass
def delete(request,**kwargs):
    pass
def view(request,**kwargs):
    print(django.utils.timezone.now)


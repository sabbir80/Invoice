from django.shortcuts import render, redirect
import django
from .forms import SaleInvoiceForm, NewSaleInvoice
from .models import *
from django.contrib import messages


# Create your views here.
def index(request, **kwargs):
    sale_invoice = SaleInvoice.objects.all()
    return render(request, 'sale_invoice_index.html', {'invoice': sale_invoice})


def sale_invoice_dashboard(request):
    return render(request, 'sale_invoice_dashboard.html')


def add(request, **kwargs):
    context = {}
    sale_invoice = SaleInvoiceForm()
    context['form'] = sale_invoice
    if request.POST:
        data = SaleInvoiceForm(request.POST)
        if data.is_valid():
            total = 0
            sale_invoice_obj = SaleInvoice.objects.get(pk=data.cleaned_data['invoice'].id)
            sale_invoice_details_obj = SaleInvoiceDetails.objects.create(sale_invoice_id=sale_invoice_obj,
                                                                         product_id=data.cleaned_data['product'],
                                                                         product_name=data.cleaned_data['product'].name,
                                                                         quantity=data.cleaned_data['quantity'],
                                                                         amount=int(data.cleaned_data['quantity'] *
                                                                                    data.cleaned_data[
                                                                                        'product'].selling_price),
                                                                         unit_price=data.cleaned_data[
                                                                             'product'].selling_price).save()

            # save total
            sale_invoice_details = SaleInvoiceDetails.objects.filter(sale_invoice_id=data.cleaned_data['invoice'])
            for i in sale_invoice_details:
                total += int(i.amount)
            sale_invoice_obj.total_amount = total
            sale_invoice_obj.save()
            messages.success(request, 'Product Added to the Sale invoice!!', extra_tags='alert')
            return redirect('new_sale_invoice_add')

    return render(request, 'sale_invoice.html', context)


def new_add(request, **kwargs):
    context = {}
    new_sale_invoice = NewSaleInvoice()
    sale_invoice = SaleInvoiceForm()
    context['new_form'] = new_sale_invoice
    context['form'] = sale_invoice
    if request.POST:
        data = NewSaleInvoice(request.POST)
        if data.is_valid():
            sale_invoice_obj = SaleInvoice.objects.create()
            sale_invoice_obj.invoice_number = data.cleaned_data['invoice_number']
            sale_invoice_obj.customer_name = data.cleaned_data['customer_name']
            sale_invoice_obj.invoice_date = data.cleaned_data['invoice_date']
            sale_invoice_details_obj = SaleInvoiceDetails.objects.create()
            sale_invoice_details_obj.product_id = data.cleaned_data['product']
            sale_invoice_details_obj.product_name = data.cleaned_data['product'].name
            sale_invoice_details_obj.sale_invoice_id = sale_invoice_obj
            sale_invoice_details_obj.quantity = data.cleaned_data['quantity']
            sale_invoice_details_obj.amount = int(
                data.cleaned_data['quantity'] * data.cleaned_data['product'].selling_price)
            sale_invoice_details_obj.unit_price = int(data.cleaned_data['product'].selling_price)
            sale_invoice_obj.total_amount = int(
                data.cleaned_data['quantity'] * data.cleaned_data['product'].selling_price)
            sale_invoice_obj.save()
            sale_invoice_details_obj.save()
            messages.success(request, 'New Sale Invoice Created Successfully!!', extra_tags='alert')
    return render(request, 'new_sale_invoice.html', context)


def edit(request, **kwargs):
    pass


def delete(request, invoice_id, **kwargs):
    Invoice = SaleInvoice.objects.get(pk=invoice_id)
    Invoice.delete()
    return redirect('sale_invoice_index')


def view(request, invoice_id, **kwargs):
    sale_invoice_details = SaleInvoiceDetails.objects.filter(sale_invoice_id=invoice_id)
    date = None
    invoice = None
    customer = None
    grandtotal = 0
    for i in sale_invoice_details:
        date = i.sale_invoice_id.invoice_date
        invoice = i.sale_invoice_id.invoice_number
        customer = i.sale_invoice_id.customer_name
        grandtotal += int(i.amount)

    return render(request, 'sale_invoice_details.html', {'invoice_details': sale_invoice_details,
                                                         'date': date,
                                                         'invoice': invoice,
                                                         'customer': customer,
                                                         'grandtotal': grandtotal})

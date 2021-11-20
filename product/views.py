from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import ProductForm
from .models import *
# Create your views here.
def index(request,**kwargs):
    data = Product.objects.all()
    return render(request,'index.html',{'product':data})
def add(request,**kwargs):
    product_form = ProductForm
    if request.POST:
        data = ProductForm(request.POST)
        if data.is_valid():
            data.save()
    return render(request,'add.html',{'product':product_form})
def edit(request,product_id,**kwargs):
    product = Product.objects.get(pk=product_id)
    product_form = ProductForm(instance=product)
    if request.POST:
        data = ProductForm(request.POST,instance=product)
        if data.is_valid():
            data.save()
            return redirect('index')
    return render(request,'add.html',{'product':product_form,
                                      'product_list':product})


def delete(request,product_id,**kwargs):
    product = Product.objects.get(pk=product_id)
    product.delete()
    return redirect('index')

def view(request,product_id,**kwargs):
    pass

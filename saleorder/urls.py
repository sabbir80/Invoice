from django.urls import path, include
from .views import *


urlpatterns = [
    path('', index, name='sale_invoice_index'),
    path('add/', add, name='sale_invoice_add'),
    path('new_sale_invoice_add/', new_add, name='new_sale_invoice_add'),
    path('<int:sale_order_id>/edit/', edit, name='sale_order_edit'),
    path('<int:invoice_id>/delete/', delete, name='sale_invoice_delete'),
    path('<int:invoice_id>', view, name='sale_invoice_details'),
    path('sale_invoice/', sale_invoice_dashboard, name='sale_invoice_dashboard'),
]
from django.urls import path, include
from .views import *


urlpatterns = [
    path('', index, name='sale_order_index'),
    path('add/', add, name='sale_order_add'),
    path('<int:sale_order_id>/edit/', edit, name='sale_order_edit'),
    path('<int:sale_order_id>/delete/', delete, name='sale_order_delete'),
    path('test/', view, name='sale_order_delete'),
]
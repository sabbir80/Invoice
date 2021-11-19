from django.urls import path, include
from .views import *


urlpatterns = [
    path('', index, name='index'),
    path('add/', add, name='product_add'),
    path('<int:product_id>/edit/', edit, name='product_edit'),
    path('<int:product_id>/delete/', delete, name='product_delete'),
    path('<int:product_id>/', view, name='product_view'),
]
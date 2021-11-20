from django.db import models
from product.models import Product
import django
# Create your models here.
class SaleInvoice(models.Model):
    invoice_number = models.CharField(max_length=200, null=True, default=None)
    invoice_date = models.DateField(default=django.utils.timezone.now)
    customer_name = models.CharField(max_length=200, null=True, default=None)
    total_amount = models.IntegerField(default=0, null=True)

    def __str__(self):
        display=''
        display += self.invoice_number+'-'+self.customer_name
        return display

class SaleInvoiceDetails(models.Model):
    sale_invoice_id = models.ForeignKey(SaleInvoice, default=None,null=True, on_delete=models.SET_NULL)
    line_number = models.IntegerField(default=None,null=True)
    product_id = models.ForeignKey(Product, default=None,null=True, on_delete=models.SET_NULL)
    product_name = models.CharField(max_length=200, default=None,null=True)
    quantity = models.IntegerField(default=0,null=True)
    unit_price = models.IntegerField(default=0,null=True)
    amount = models.CharField(max_length=200,default=None,null=True)

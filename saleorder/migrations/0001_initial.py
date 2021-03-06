# Generated by Django 3.2.9 on 2021-11-18 17:41

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0002_alter_product_selling_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='SaleInvoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invoice_number', models.CharField(default=None, max_length=200, null=True)),
                ('invoice_date', models.DateField(default=django.utils.timezone.now)),
                ('customer_name', models.CharField(default=None, max_length=200, null=True)),
                ('total_amount', models.IntegerField(default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SaleInvoiceDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('line_number', models.IntegerField(default=None, null=True)),
                ('product_name', models.CharField(default=None, max_length=200, null=True)),
                ('quantity', models.IntegerField(default=0, null=True)),
                ('unit_price', models.IntegerField(default=0, null=True)),
                ('amount', models.CharField(default=None, max_length=200, null=True)),
                ('product_id', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.product')),
                ('sale_invoice_id', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='saleorder.saleinvoice')),
            ],
        ),
    ]

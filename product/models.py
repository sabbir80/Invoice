from django.db import models


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255, default=None, null=True)
    code = models.CharField(max_length=255, default=None, null=True)
    selling_price = models.IntegerField(default=None, null=True)

    def __str__(self):
        return self.name


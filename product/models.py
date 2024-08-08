from django.db import models

# Create your models here.

class Product(models.Model):
    name=models.CharField(max_length=100,verbose_name="Ürün İsmi")
    image=models.FileField(upload_to="Products",blank=True,null=True)

    def __str__(self):
        return self.name

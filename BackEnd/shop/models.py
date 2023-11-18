from django.db import models
from datetime import datetime

class ProductCategory(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=50)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    price = models.IntegerField(default=0)
    pub_date = models.DateField(default=datetime.now().strftime("%Y-%m-%d"), blank=True, null=True)
    image = models.ImageField(upload_to="shop/images", default="")

    def __str__(self):
        return self.product_name

    def save(self, *args, **kwargs):
        # Set the image name same as the product_name
        if self.image and self.product_name:
            ext = self.image.name.split('.')[-1]
            self.image.name = f"{self.product_name}.{ext}"
        super().save(*args, **kwargs)
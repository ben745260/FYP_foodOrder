import os
from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

def get_image_path(instance, filename):
    if instance.pk is not None:
        # Use the existing filename when the model is being updated
        old_instance = Product.objects.get(pk=instance.pk)
        if old_instance.image:
            return old_instance.image.path

    # Use the original upload_to parameter when the model is being created or the image field is empty
    return os.path.join("shop/images", filename)


class ProductCategory(models.Model):
    category_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=50)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, null=True)
    price = models.IntegerField(default=0)
    product_detail = models.CharField(max_length=500, default="", null=True, blank=True)
    pub_date = models.DateField(default=datetime.now().strftime("%Y-%m-%d"), blank=True, null=True)
    image = models.ImageField(upload_to=get_image_path, null=True, blank=True)

    def __str__(self):
        return self.product_name

    def save(self, *args, **kwargs):
        # Set the image name same as the product_name
        if self.image and self.product_name:
            ext = self.image.name.split('.')[-1]
            self.image.name = f"{self.product_name}.{ext}"
        super().save(*args, **kwargs)


class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    order_user = models.ForeignKey(User, on_delete=models.CASCADE)
    order_items = models.ManyToManyField(Product)
    order_lastEditor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='last_editor')
    order_lastUpdateTime = models.DateField(default=datetime.now().strftime("%Y-%m-%d"), blank=True, null=True)

    def __str__(self):
        return str(self.order_user.username)
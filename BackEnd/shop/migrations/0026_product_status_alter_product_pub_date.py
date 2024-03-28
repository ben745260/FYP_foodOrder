# Generated by Django 4.2.7 on 2024-03-28 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0025_alter_product_pub_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='status',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='pub_date',
            field=models.DateField(blank=True, default='2024-03-28', null=True),
        ),
    ]

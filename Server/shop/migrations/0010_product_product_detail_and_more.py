# Generated by Django 4.2.7 on 2024-01-25 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_alter_product_pub_date_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_detail',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_lastUpdateTime',
            field=models.DateField(blank=True, default='2024-01-25', null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='pub_date',
            field=models.DateField(blank=True, default='2024-01-25', null=True),
        ),
    ]

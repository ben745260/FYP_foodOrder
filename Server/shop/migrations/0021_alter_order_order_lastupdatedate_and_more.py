# Generated by Django 4.2.7 on 2024-03-12 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0020_order_order_lastupdatedate_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_lastUpdateDate',
            field=models.DateField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_lastUpdateTime',
            field=models.TimeField(auto_now=True, null=True),
        ),
    ]
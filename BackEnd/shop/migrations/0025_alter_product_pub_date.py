# Generated by Django 4.2.7 on 2024-03-20 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0024_userfeedback_alter_product_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='pub_date',
            field=models.DateField(blank=True, default='2024-03-20', null=True),
        ),
    ]

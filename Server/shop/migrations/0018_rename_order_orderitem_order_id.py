# Generated by Django 4.2.7 on 2024-03-09 13:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0017_rename_order_id_orderitem_order'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderitem',
            old_name='order',
            new_name='order_id',
        ),
    ]

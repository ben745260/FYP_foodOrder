# Generated by Django 4.2.7 on 2023-11-18 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=50)),
                ('category', models.CharField(default='', max_length=50)),
                ('price', models.IntegerField(default=0)),
                ('pub_date', models.DateField(blank=True, default='2023-11-18 16:46', null=True)),
                ('image', models.ImageField(default='', upload_to='shop/images')),
            ],
        ),
    ]

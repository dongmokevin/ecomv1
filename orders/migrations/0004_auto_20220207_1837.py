# Generated by Django 3.1 on 2022-02-07 23:37

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_auto_20210301_1833'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None),
        ),
    ]

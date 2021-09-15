# Generated by Django 3.2.6 on 2021-09-14 00:54

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visitor',
            name='checkin',
            field=models.DateTimeField(default='2021-09-14 08:54:17', editable=False),
        ),
        migrations.AlterField(
            model_name='visitor',
            name='emergency_phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None, unique=True),
        ),
        migrations.AlterField(
            model_name='visitor',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True),
        ),
    ]

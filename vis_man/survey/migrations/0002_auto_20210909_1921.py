# Generated by Django 3.2.6 on 2021-09-09 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='site',
            old_name='sites',
            new_name='visitors',
        ),
        migrations.AlterField(
            model_name='visitor',
            name='checkin',
            field=models.DateTimeField(default='2021-09-09 19:21:31', editable=False),
        ),
    ]

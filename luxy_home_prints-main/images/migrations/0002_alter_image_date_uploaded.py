# Generated by Django 4.0.4 on 2022-08-19 03:37

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='date_uploaded',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 19, 3, 37, 51, 648755, tzinfo=utc), verbose_name='Upload date'),
        ),
    ]

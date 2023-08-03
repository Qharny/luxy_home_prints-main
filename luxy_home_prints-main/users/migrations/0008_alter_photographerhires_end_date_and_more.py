# Generated by Django 4.0.4 on 2022-08-09 03:18

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_alter_photographerhires_end_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photographerhires',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 9, 3, 18, 13, 508275, tzinfo=utc), verbose_name='End date'),
        ),
        migrations.AlterField(
            model_name='photographerhires',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 9, 3, 18, 13, 508275, tzinfo=utc), verbose_name='Start date'),
        ),
        migrations.AlterField(
            model_name='user',
            name='token_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 9, 3, 18, 13, 508275, tzinfo=utc), verbose_name='date published'),
        ),
    ]
# Generated by Django 4.0.4 on 2022-07-29 05:00

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_photo_alter_user_options_user_address_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='name',
            field=models.CharField(max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='photographerhires',
            name='client_id',
            field=models.CharField(max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='photographerhires',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 29, 5, 0, 42, 865640, tzinfo=utc), verbose_name='End date'),
        ),
        migrations.AlterField(
            model_name='photographerhires',
            name='pricing_period',
            field=models.CharField(max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='photographerhires',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 29, 5, 0, 42, 865640, tzinfo=utc), verbose_name='Start date'),
        ),
        migrations.AlterField(
            model_name='user',
            name='address',
            field=models.CharField(max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='pricing_period',
            field=models.CharField(max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='region',
            field=models.CharField(max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='token_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 29, 5, 0, 42, 865640, tzinfo=utc), verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='user',
            name='town',
            field=models.CharField(max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='workday_end',
            field=models.CharField(max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='workday_start',
            field=models.CharField(max_length=25, null=True),
        ),
    ]

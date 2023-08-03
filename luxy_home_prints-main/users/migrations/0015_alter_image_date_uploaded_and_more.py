# Generated by Django 4.0.4 on 2022-08-17 18:17

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0014_alter_image_date_uploaded_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='date_uploaded',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 17, 18, 17, 41, 775697, tzinfo=utc), verbose_name='Upload date'),
        ),
        migrations.AlterField(
            model_name='photographerhires',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 17, 18, 17, 41, 772692, tzinfo=utc), verbose_name='End date'),
        ),
        migrations.AlterField(
            model_name='photographerhires',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 17, 18, 17, 41, 772692, tzinfo=utc), verbose_name='Start date'),
        ),
        migrations.AlterField(
            model_name='user',
            name='token_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 17, 18, 17, 41, 768694, tzinfo=utc), verbose_name='date published'),
        ),
    ]

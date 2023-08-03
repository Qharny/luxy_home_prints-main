# Generated by Django 4.0.4 on 2022-08-09 11:14

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_alter_image_date_uploaded_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='categories',
            name='icon',
            field=models.ImageField(null=True, upload_to='icons/categories'),
        ),
        migrations.AlterField(
            model_name='image',
            name='date_uploaded',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 9, 11, 14, 52, 358733, tzinfo=utc), verbose_name='Upload date'),
        ),
        migrations.AlterField(
            model_name='photographerhires',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 9, 11, 14, 52, 358733, tzinfo=utc), verbose_name='End date'),
        ),
        migrations.AlterField(
            model_name='photographerhires',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 9, 11, 14, 52, 358733, tzinfo=utc), verbose_name='Start date'),
        ),
        migrations.AlterField(
            model_name='user',
            name='token_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 9, 11, 14, 52, 358733, tzinfo=utc), verbose_name='date published'),
        ),
    ]

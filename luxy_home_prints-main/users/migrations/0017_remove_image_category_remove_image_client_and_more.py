# Generated by Django 4.0.4 on 2022-08-19 03:28

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0016_alter_image_date_uploaded_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='category',
        ),
        migrations.RemoveField(
            model_name='image',
            name='client',
        ),
        migrations.AlterField(
            model_name='photographerhires',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 19, 3, 28, 48, 907148, tzinfo=utc), verbose_name='End date'),
        ),
        migrations.AlterField(
            model_name='photographerhires',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 19, 3, 28, 48, 907148, tzinfo=utc), verbose_name='Start date'),
        ),
        migrations.AlterField(
            model_name='user',
            name='token_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 19, 3, 28, 48, 885149, tzinfo=utc), verbose_name='date published'),
        ),
        migrations.DeleteModel(
            name='Categories',
        ),
        migrations.DeleteModel(
            name='Image',
        ),
    ]

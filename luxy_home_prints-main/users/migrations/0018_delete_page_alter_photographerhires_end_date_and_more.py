# Generated by Django 4.0.4 on 2022-08-19 03:37

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0017_remove_image_category_remove_image_client_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Page',
        ),
        migrations.AlterField(
            model_name='photographerhires',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 19, 3, 37, 51, 642755, tzinfo=utc), verbose_name='End date'),
        ),
        migrations.AlterField(
            model_name='photographerhires',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 19, 3, 37, 51, 642755, tzinfo=utc), verbose_name='Start date'),
        ),
        migrations.AlterField(
            model_name='user',
            name='token_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 19, 3, 37, 51, 615587, tzinfo=utc), verbose_name='date published'),
        ),
    ]
# Generated by Django 4.0.4 on 2022-07-23 04:34

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_remove_user_auth_status_user_token_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='token_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 23, 4, 34, 54, 601414, tzinfo=utc), verbose_name='date published'),
        ),
    ]

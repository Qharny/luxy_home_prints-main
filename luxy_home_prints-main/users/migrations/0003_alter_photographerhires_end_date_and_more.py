# Generated by Django 4.0.4 on 2022-08-07 04:46

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_photographerhires_end_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photographerhires',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 7, 4, 46, 26, 958572, tzinfo=utc), verbose_name='End date'),
        ),
        migrations.AlterField(
            model_name='photographerhires',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 7, 4, 46, 26, 958572, tzinfo=utc), verbose_name='Start date'),
        ),
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(null=True, upload_to='avatar'),
        ),
        migrations.AlterField(
            model_name='user',
            name='token_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 7, 4, 46, 26, 896060, tzinfo=utc), verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='user',
            name='workday_end',
            field=models.CharField(choices=[('mon', 'Monday'), ('tue', 'Tuesday'), ('wed', 'Wednesday'), ('thu', 'Thursday'), ('fri', 'Friday'), ('sat', 'Saturday'), ('sun', 'Sunday')], max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='workday_start',
            field=models.CharField(choices=[('mon', 'Monday'), ('tue', 'Tuesday'), ('wed', 'Wednesday'), ('thu', 'Thursday'), ('fri', 'Friday'), ('sat', 'Saturday'), ('sun', 'Sunday')], max_length=25, null=True),
        ),
    ]
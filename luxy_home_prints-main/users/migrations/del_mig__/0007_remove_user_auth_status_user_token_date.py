# Generated by Django 4.0.4 on 2022-07-11 08:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_user_auth_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='auth_status',
        ),
        migrations.AddField(
            model_name='user',
            name='token_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='date published'),
            preserve_default=False,
        ),
    ]

# Generated by Django 4.0.4 on 2022-07-11 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_rename_auth_code_user_auth_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='auth_status',
            field=models.IntegerField(default=0),
        ),
    ]
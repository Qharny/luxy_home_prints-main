# Generated by Django 4.0.4 on 2022-07-10 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_rename_authtoken_user_auth_token_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='auth_code',
            field=models.IntegerField(default=0, max_length=1),
        ),
        migrations.AlterField(
            model_name='user',
            name='auth_type',
            field=models.CharField(default='', max_length=10),
        ),
    ]

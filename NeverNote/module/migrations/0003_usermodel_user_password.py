# Generated by Django 5.1.1 on 2024-10-04 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('module', '0002_usermodel_timestamp_alter_usermodel_user_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermodel',
            name='user_password',
            field=models.CharField(max_length=128, default='default_password'),
        ),
    ]
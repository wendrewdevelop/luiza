# Generated by Django 5.0 on 2023-12-08 23:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_admin'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='username',
        ),
    ]
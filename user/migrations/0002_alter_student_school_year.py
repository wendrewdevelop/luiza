# Generated by Django 5.0 on 2023-12-13 19:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school_year', '0001_initial'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='school_year',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='school_year.schoolyear'),
        ),
    ]

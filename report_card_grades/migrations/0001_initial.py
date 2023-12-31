# Generated by Django 5.0 on 2023-12-12 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ReportCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Nota do aluno')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'report_card',
                'verbose_name_plural': 'reports_card',
                'db_table': 'tb_report_card',
            },
        ),
    ]

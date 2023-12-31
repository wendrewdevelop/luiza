# Generated by Django 5.0 on 2023-12-12 20:43

import django.db.models.deletion
import user.managers
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=30, verbose_name='last name')),
                ('user_type', models.CharField(blank=True, choices=[('aluno', 'Aluno'), ('professor', 'Professor'), ('admin', 'Administrativo')], max_length=60, null=True, verbose_name='user type')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='date joined')),
                ('is_active', models.BooleanField(default=True, verbose_name='active')),
                ('is_staff', models.BooleanField(default=True, verbose_name='staff')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'db_table': 'tb_user',
            },
            managers=[
                ('objects', user.managers.CustomUserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('school_position', models.CharField(blank=True, max_length=100, null=True, verbose_name='Cargo')),
                ('status', models.CharField(blank=True, choices=[('active', 'Ativo'), ('inactive', 'Inativo')], default='active', max_length=60, null=True, verbose_name='Ano escolar')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('school_year', models.CharField(blank=True, choices=[('1a', 'Primeiro Ano'), ('2a', 'Segundo Ano'), ('3a', 'Terceiro Ano'), ('4a', 'Quarto Ano'), ('5a', 'Quinto Ano'), ('6a', 'Sexto Ano'), ('7a', 'Sétimo Ano'), ('8a', 'Oitavo Ano'), ('9a', 'Nono Ano'), ('1c', 'Primeiro Colegial'), ('2c', 'Segundo Colegial'), ('3c', 'Terceiro Colegial')], max_length=60, null=True, verbose_name='Ano escolar')),
                ('status', models.CharField(blank=True, choices=[('active', 'Ativo'), ('graduated', 'Graduado'), ('inactive', 'Inativo')], default='active', max_length=60, null=True, verbose_name='Ano escolar')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('school_subject', models.CharField(blank=True, max_length=100, null=True, verbose_name='Matéria')),
                ('status', models.CharField(blank=True, choices=[('active', 'Ativo'), ('inactive', 'Inativo')], default='active', max_length=60, null=True, verbose_name='Ano escolar')),
            ],
        ),
    ]

from django.db import models


class SchoolYear(models.Model):
    STUDENT_SCHOOL_YEAR = [
        ('1a', 'Primeiro Ano'),
        ('2a', 'Segundo Ano'),
        ('3a', 'Terceiro Ano'),
        ('4a', 'Quarto Ano'),
        ('5a', 'Quinto Ano'),
        ('6a', 'Sexto Ano'),
        ('7a', 'Sétimo Ano'),
        ('8a', 'Oitavo Ano'),
        ('9a', 'Nono Ano'),
        ('1c', 'Primeiro Colegial'),
        ('2c', 'Segundo Colegial'),
        ('3c', 'Terceiro Colegial')
    ]

    year = models.CharField(
        'Ano escolar',
        choices=STUDENT_SCHOOL_YEAR,
        max_length=255,
        null=False,
        blank=False
    )

    class Meta:
        verbose_name = 'school_year'
        verbose_name_plural = 'school_years'
        db_table = 'tb_school_year'

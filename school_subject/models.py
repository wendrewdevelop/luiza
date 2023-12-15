from django.db import models


class Subject(models.Model):
    subject = models.CharField(
        'Matéria',
        max_length=30,
        blank=True,
        null=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'subject'
        verbose_name_plural = 'subjects'
        db_table = 'tb_subject'
from django.db import models
from user.models import User


class ReportCard(models.Model):
    student = models.ForeignKey(
        User,
        verbose_name='Aluno',
        on_delete=models.PROTECT,
        blank=True,
        null=True,
    )
    grade = models.DecimalField(
        'Nota do aluno',
        max_digits=10,
        decimal_places=2
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'report_card'
        verbose_name_plural = 'reports_card'
        db_table = 'tb_report_card'

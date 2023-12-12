from django.db import models
from user.models import User


class ReportCard(models.Model):
    ...
    """
        user = get_object_or_404(User, email=email)
        if self.request.user.user_type == 'student':
            return Response({'error': 'Você não tem autorização para realizar essa ação.'}, status=status.HTTP_403_FORBIDDEN)
        student = get_object_or_404(Student, user=user)

        report_card = ReportCard.objects.create(
            student = student,
            ...
        )
    """

    student = models.ForeignKey(
        User,
        verbose_name='Agente responsável por resolver',
        on_delete=models.CASCADE,
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

from django.db import models
from user.models import User


class Administrative(models.Model):
    """
        Modelo para registrar apenas as ações 
        administrativas feitas na aplicação.

        Example:
            action = Criação da turma do 3 colegial
            model_name = obj._meta.model_name
    """

    user = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        null=False,
        blank=False
    )
    action = models.CharField(
        'Ação que foi realizada',
        max_length=130,
        null=False,
        blank=False
    )
    model_name = models.CharField(
        'Nome do modelo que foi afetado',
        max_length=130,
        null=True,
        blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'admin'
        verbose_name_plural = 'admins'
        db_table = 'tb_admin'



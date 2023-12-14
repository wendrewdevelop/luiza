from django.db import models


class Rules(models.Model):
    rule_type = models.CharField(
        'Tipe de regra criada',
        max_length=255,
        null=False,
        blank=False
    )
    rule_description = models.CharField(
        'Descrição',
        max_length=255,
        null=False,
        blank=False
    )
    rule_action = models.CharField(
        'Ação realizada',
        max_length=255,
        null=False,
        blank=False
    )

    class Meta:
        verbose_name = 'rules'
        verbose_name_plural = 'rules'
        db_table = 'tb_rule'

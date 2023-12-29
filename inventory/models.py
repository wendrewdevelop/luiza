from django.db import models
from user.models import User
from school_subject.models import Subject


class Inventory(models.Model):
    item_name = models.CharField(
        'Nome do item',
        max_length=100
    )
    description = models.CharField(
        'Descrição do item',
        max_length=600,
        blank=True,
        null=True,
    )
    duedate = models.DateField(
        blank=True,
        null=True
    )
    created_by = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        blank=True,
        null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'inventory'
        verbose_name_plural = 'inventories'
        db_table = 'tb_inventory'

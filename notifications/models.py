from django.db import models


class Notification(models.Model):
    """
        After user create, edit register on this model.    
    """

    title = models.CharField(
        'Titulo da notificação',
        max_length=100,
        null=True,
        blank=True
    )
    message = models.CharField(
        'Conteudo da notificação',
        max_length=600,
        null=True,
        blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'notification'
        verbose_name_plural = 'notifications'
        db_table = 'tb_notification'

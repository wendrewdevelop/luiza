from django.db import models
from user.models import User


class Scheduler(models.Model):
    VISIBILITY_LIST = [
        ('public', 'Publico'),
        ('private', 'Somente eu')
    ]

    created_by = models.ForeignKey(
        User,
        verbose_name='Usuário',
        on_delete=models.PROTECT,
        blank=False,
        null=False,
    )
    day = models.IntegerField(
        'dia',
        null=False,
        blank=False
    )
    month = models.CharField(
        'mês',
        max_length=30,
        null=False,
        blank=False
    )
    year = models.IntegerField(
        'ano',
        null=False,
        blank=False
    )
    title = models.CharField(
        'titulo do evento',
        max_length=30,
        null=False,
        blank=False
    )
    description = models.CharField(
        'descrição do evento',
        max_length=30,
        null=True,
        blank=True
    )
    visibility = models.CharField(
        'quem pode ver o evento',
        choices=VISIBILITY_LIST,
        max_length=30,
        null=False,
        blank=False,
        default='private'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'scheduler'
        verbose_name_plural = 'schedulers'
        db_table = 'tb_scheduler'

    @property
    def can_see_item(self, user):
        if self.visibility == 'private':
            # Only the user who created the item can see it
            return user == self.created_by
        elif self.visibility == 'public':
            # Everyone can see the item
            return True
        elif self.visibility == 'for_students':
            # Only students can see the item
            return hasattr(user, 'student')  # Assuming you have a 'Student' related model
        elif self.visibility == 'for_teacher':
            # Only teachers can see the item
            return hasattr(user, 'teacher')  # Assuming you have a 'Teacher' related model
        else:
            # Handle other cases or raise an exception if needed
            return False

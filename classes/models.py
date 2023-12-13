from django.db import models
from user.models import User
from school_year.models import SchoolYear


class Video(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    video_file = models.FileField(upload_to='videos/')
    school_year = models.ForeignKey(
        SchoolYear,
        on_delete=models.PROTECT,
        null=False,
        blank=False
    )

    class Meta:
        verbose_name = 'video'
        verbose_name_plural = 'videos'
        db_table = 'tb_video'

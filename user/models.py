from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from rest_framework.authtoken.models import Token
from .managers import CustomUserManager


class User(AbstractUser):
    USER_TYPE_CHOICES = [
        ('aluno', 'Aluno'),
        ('professor', 'Professor'),
        ('admin', 'Administrativo'),
    ]
    
    email = models.EmailField('email address', unique=True)
    username = None
    first_name = models.CharField('first name', max_length=30, blank=True)
    last_name = models.CharField('last name', max_length=30, blank=True)
    user_type = models.CharField(
        'user type',
        max_length=60,
        choices=USER_TYPE_CHOICES,
        null=True,
        blank=True
    )
    date_joined = models.DateTimeField('date joined', auto_now_add=True)
    is_active = models.BooleanField('active', default=True)
    is_staff = models.BooleanField('staff', default=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
        db_table = 'tb_user'


@receiver(post_save, sender=get_user_model())
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        if instance.user_type == 'student':
            Student.objects.create(user=instance)
        elif instance.user_type == 'teacher':
            Teacher.objects.create(user=instance)
        elif instance.user_type == 'admin':
            Admin.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    if instance.user_type == 'student':
        instance.student.save()
    elif instance.user_type == 'teacher':
        instance.teacher.save()
    elif instance.user_type == 'admin':
        instance.admin.save()


class Student(models.Model):
    """
        After user create, edit register on this model.    
    """

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
    STUDENT_STATUS_LIST = [
        ('active', 'Ativo'),
        ('graduated', 'Graduado'),
        ('inactive', 'Inativo')
    ]

    user = models.OneToOneField(
        User, 
        on_delete=models.CASCADE, 
        primary_key=True
    )
    school_year = models.CharField(
        'Ano escolar',
        max_length=60,
        choices=STUDENT_SCHOOL_YEAR,
        null=True,
        blank=True
    )
    status = models.CharField(
        'Ano escolar',
        max_length=60,
        choices=STUDENT_STATUS_LIST,
        null=True,
        blank=True,
        default='active'
    )

    def __str__(self):
        return f"Student: {self.user.email}"


class Teacher(models.Model):
    """
        After user create, edit register on this model.    
    """

    TEACHER_STATUS_LIST = [
        ('active', 'Ativo'),
        ('inactive', 'Inativo')
    ]

    user = models.OneToOneField(
        User, 
        on_delete=models.CASCADE, 
        primary_key=True
    )
    school_subject = models.CharField(
        'Matéria',
        max_length=100,
        null=True,
        blank=True
    )
    status = models.CharField(
        'Ano escolar',
        max_length=60,
        choices=TEACHER_STATUS_LIST,
        null=True,
        blank=True,
        default='active'
    )

    def __str__(self):
        return f"Teacher: {self.user.email}"


class Admin(models.Model):
    """
        After user create, edit register on this model.    
    """

    ADMIN_STATUS_LIST = [
        ('active', 'Ativo'),
        ('inactive', 'Inativo')
    ]

    user = models.OneToOneField(
        User, 
        on_delete=models.CASCADE, 
        primary_key=True
    )
    school_position = models.CharField(
        'Cargo',
        max_length=100,
        null=True,
        blank=True
    )
    status = models.CharField(
        'Ano escolar',
        max_length=60,
        choices=ADMIN_STATUS_LIST,
        null=True,
        blank=True,
        default='active'
    )

    def __str__(self):
        return f"Admin: {self.user.email}"
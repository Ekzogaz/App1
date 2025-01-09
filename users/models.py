from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    image = models.ImageField(
        upload_to='users/images',
        default="", 
        blank=True,
        null=True,
        verbose_name='Аватар'
    )

    class Meta:
        db_table = 'user'
        verbose_name = 'Пользователя'
        verbose_name_plural = 'Пользователи'# Create your models here.

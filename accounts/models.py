from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    POS = (
        ('STUDENT', 'Магистрант'),
        ('ADMIN', 'Педагог')
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    image = models.ImageField(verbose_name='Изображение', blank=True, null=True, upload_to='accounts/profile/')
    position = models.CharField(verbose_name='Позиция', choices=POS, default=POS[0][1], max_length=64)

    def __str__(self):
        return f'Профиль: {self.user.username}'

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

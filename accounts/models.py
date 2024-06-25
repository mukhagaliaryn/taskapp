from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    POS = (
        ('STAFF', 'Сотрудник'),
        ('ADMIN', 'Администрация')
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    image = models.ImageField(verbose_name='Изображение', blank=True, null=True, upload_to='accounts/profile/')
    position = models.CharField(verbose_name='Позиция', choices=POS, default=POS[0][1], max_length=64)
    profession = models.CharField(verbose_name='Профессия', max_length=64, default='')

    def __str__(self):
        return f'Профиль: {self.user.first_name} {self.user.last_name}'

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

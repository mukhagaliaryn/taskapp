from django.db import models
from django.contrib.auth.models import User


class Session(models.Model):
    title = models.CharField(verbose_name='Название', max_length=64, default='n-аралық')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Сессия'
        verbose_name_plural = 'Сессии'


class Weekend(models.Model):
    title = models.CharField(verbose_name='Название', max_length=64, default='n-апта')
    session = models.ForeignKey(Session, on_delete=models.CASCADE, verbose_name='Аралық/Сессия')
    is_open = models.BooleanField(verbose_name='Открыто', default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Лента'
        verbose_name_plural = 'Ленты'


class Task(models.Model):
    title = models.CharField(verbose_name='Название тема', max_length=64)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    weekend = models.ForeignKey(Weekend, on_delete=models.CASCADE, verbose_name='Лента')

    file = models.FileField(verbose_name='Исходный файл', upload_to='tasks/files/')
    description = models.TextField(verbose_name='Описание', blank=True, null=True)
    is_send = models.BooleanField(verbose_name='Отправлено', default=False)
    date_created = models.DateTimeField(verbose_name='Дата добавление', auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

from django.db import models
from django.contrib.auth.models import User


class Project(models.Model):
    STATUS = (
        ('START', 'На старте'),
        ('PROCESS', 'В процессе'),
        ('FINISH', 'Завершено'),
    )

    title = models.CharField(verbose_name='Название', max_length=255)
    description = models.TextField(verbose_name='Описание', blank=True, null=True)
    status = models.CharField(verbose_name='Статус', max_length=64, choices=STATUS, default=STATUS[0][1])
    date_created = models.DateTimeField(verbose_name='Дата добавление', auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'


class Task(models.Model):
    STATUS = (
        ('PROCESS', 'В процессе'),
        ('FINISH', 'Завершено'),
    )
    project = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name='Проект')
    title = models.CharField(verbose_name='Название задачи', max_length=255, default='#n ...')
    description = models.TextField(verbose_name='Описание', blank=True, null=True)
    status = models.CharField(verbose_name='Статус', max_length=64, choices=STATUS, default=STATUS[0][1])
    date_created = models.DateTimeField(verbose_name='Дата создание', auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'


class Solution(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, verbose_name='Задача')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    description = models.TextField(verbose_name='Описание', blank=True, null=True)
    file = models.FileField(verbose_name='Исходный файл', upload_to='tasks/files/')
    is_send = models.BooleanField(verbose_name='Отправлено', default=False)
    date_created = models.DateTimeField(verbose_name='Дата добавление', auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Решение'
        verbose_name_plural = 'Решения'

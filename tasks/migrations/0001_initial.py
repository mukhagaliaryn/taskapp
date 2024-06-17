# Generated by Django 4.1.7 on 2024-06-17 05:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('status', models.CharField(choices=[('STAFF', 'Сотрудник'), ('ADMIN', 'Администрация')], default='Сотрудник', max_length=64, verbose_name='Статус')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Дата добавление')),
            ],
            options={
                'verbose_name': 'Проект',
                'verbose_name_plural': 'Проекты',
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название задачи')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('status', models.CharField(choices=[('STAFF', 'Сотрудник'), ('ADMIN', 'Администрация')], default='Сотрудник', max_length=64, verbose_name='Статус')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создание')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.project', verbose_name='Проект')),
            ],
            options={
                'verbose_name': 'Задача',
                'verbose_name_plural': 'Задачи',
            },
        ),
        migrations.CreateModel(
            name='Solution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название задачи')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('file', models.FileField(upload_to='tasks/files/', verbose_name='Исходный файл')),
                ('is_send', models.BooleanField(default=False, verbose_name='Отправлено')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Дата добавление')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.task', verbose_name='Задача')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Решение',
                'verbose_name_plural': 'Решения',
            },
        ),
    ]

# Generated by Django 4.1.7 on 2023-02-14 12:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='n-аралық', max_length=64, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Сессия',
                'verbose_name_plural': 'Сессии',
            },
        ),
        migrations.CreateModel(
            name='Weekend',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='n-апта', max_length=64, verbose_name='Название')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.session', verbose_name='Аралық/Сессия')),
            ],
            options={
                'verbose_name': 'Лента',
                'verbose_name_plural': 'Ленты',
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, verbose_name='Название тема')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('weekend', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.weekend', verbose_name='Апталық')),
            ],
            options={
                'verbose_name': 'Задача',
                'verbose_name_plural': 'Задачи',
            },
        ),
    ]
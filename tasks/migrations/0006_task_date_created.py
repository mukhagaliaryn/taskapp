# Generated by Django 4.1.7 on 2023-02-15 06:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0005_weekend_is_open'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Дата добавление'),
            preserve_default=False,
        ),
    ]

# Generated by Django 4.1.7 on 2023-02-15 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_task_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='is_send',
            field=models.BooleanField(default=False, verbose_name='Отправлено'),
        ),
    ]

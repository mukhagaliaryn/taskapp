# Generated by Django 4.1.7 on 2023-02-15 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_task_user_alter_task_weekend'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='file',
            field=models.FileField(default=1, upload_to='tasks/files/', verbose_name='Исходный файл'),
            preserve_default=False,
        ),
    ]
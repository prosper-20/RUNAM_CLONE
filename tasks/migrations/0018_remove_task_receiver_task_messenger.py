# Generated by Django 4.1.7 on 2023-05-01 11:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tasks', '0017_alter_task_receiver'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='receiver',
        ),
        migrations.AddField(
            model_name='task',
            name='messenger',
            field=models.ForeignKey(default=4, on_delete=django.db.models.deletion.CASCADE, related_name='the_task_messenger', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]

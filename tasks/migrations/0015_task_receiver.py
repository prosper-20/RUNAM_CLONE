# Generated by Django 4.1.7 on 2023-05-01 11:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tasks', '0014_task_task_bidders'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='receiver',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='the_task_receiver', to=settings.AUTH_USER_MODEL),
        ),
    ]

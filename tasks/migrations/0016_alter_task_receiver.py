# Generated by Django 4.1.7 on 2023-05-01 11:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tasks', '0015_task_receiver'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='receiver',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='the_task_receiver', to=settings.AUTH_USER_MODEL),
        ),
    ]

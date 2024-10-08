# Generated by Django 4.0.5 on 2024-08-28 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_task_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='price',
            field=models.DecimalField(decimal_places=2, default=20, max_digits=12),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='task',
            name='tip',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]

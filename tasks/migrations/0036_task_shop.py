# Generated by Django 4.1.7 on 2023-06-21 09:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0035_shopdocuments_shopimages_shopprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='shop',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tasks.shop'),
        ),
    ]

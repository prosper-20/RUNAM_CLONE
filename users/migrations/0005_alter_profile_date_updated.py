# Generated by Django 4.1.7 on 2023-03-31 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_profile_date_updated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='date_updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]

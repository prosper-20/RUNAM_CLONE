# Generated by Django 4.1.7 on 2023-05-08 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_rename_is_staff_user_admin_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='location',
            field=models.CharField(default='Lagos', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='phone_number',
            field=models.CharField(default='09036356792', max_length=11),
            preserve_default=False,
        ),
    ]

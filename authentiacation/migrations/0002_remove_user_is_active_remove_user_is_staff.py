# Generated by Django 4.1.3 on 2022-11-19 10:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentiacation', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_staff',
        ),
    ]

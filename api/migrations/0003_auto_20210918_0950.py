# Generated by Django 3.2.7 on 2021-09-18 09:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_uploadmodel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='uploadmodel',
            name='password',
        ),
        migrations.RemoveField(
            model_name='uploadmodel',
            name='username',
        ),
    ]
# Generated by Django 2.0.4 on 2018-04-11 10:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Tunes', '0002_auto_20180411_0549'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='other_events',
        ),
    ]
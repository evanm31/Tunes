# Generated by Django 2.0.4 on 2018-04-11 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tunes', '0003_remove_event_other_events'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='other_events',
            field=models.ManyToManyField(related_name='other_events_occuring', to='Tunes.Event'),
        ),
    ]

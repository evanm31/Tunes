# Generated by Django 2.0.2 on 2018-03-08 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tunes', '0008_auto_20180308_1625'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='user',
            name='events_attended',
            field=models.ManyToManyField(blank=True, null=True, related_name='user_events_attended', to='Tunes.Event'),
        ),
        migrations.AlterField(
            model_name='user',
            name='events_attending',
            field=models.ManyToManyField(blank=True, null=True, related_name='user_events_attending', to='Tunes.Event'),
        ),
        migrations.RemoveField(
            model_name='user',
            name='events_hosting',
        ),
        migrations.AddField(
            model_name='user',
            name='events_hosting',
            field=models.ManyToManyField(blank=True, null=True, related_name='user_events_hosting', to='Tunes.Event'),
        ),
        migrations.AlterField(
            model_name='user',
            name='followers',
            field=models.ManyToManyField(blank=True, null=True, related_name='user_followers', to='Tunes.User'),
        ),
        migrations.AlterField(
            model_name='user',
            name='following',
            field=models.ManyToManyField(blank=True, null=True, related_name='user_following', to='Tunes.User'),
        ),
    ]

# Generated by Django 5.1.1 on 2024-10-09 23:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0009_album_band_event_band_song_band_remove_event_artist_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='is_band_member',
            field=models.BooleanField(default=False),
        ),
    ]

# Generated by Django 4.1.2 on 2022-10-29 04:44

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('musicapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='artiste',
            name='age',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='artiste',
            name='first_name',
            field=models.CharField(blank=True, max_length=400),
        ),
        migrations.AddField(
            model_name='artiste',
            name='last_name',
            field=models.CharField(blank=True, max_length=400),
        ),
        migrations.AddField(
            model_name='lyric',
            name='content',
            field=models.CharField(blank=True, max_length=400),
        ),
        migrations.AddField(
            model_name='lyric',
            name='song_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='musicapp.song'),
        ),
        migrations.AddField(
            model_name='song',
            name='artiste_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='musicapp.artiste'),
        ),
        migrations.AddField(
            model_name='song',
            name='date_released',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='song',
            name='likes',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='song',
            name='title',
            field=models.CharField(blank=True, max_length=400),
        ),
    ]

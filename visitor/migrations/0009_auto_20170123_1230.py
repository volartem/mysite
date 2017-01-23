# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-23 12:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visitor', '0008_auto_20170123_1209'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='visitor',
            name='avatar',
        ),
        migrations.AddField(
            model_name='visitor',
            name='Uid',
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='visitor',
            name='provider',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='visitor',
            name='user_img_url',
            field=models.SlugField(default=''),
        ),
    ]

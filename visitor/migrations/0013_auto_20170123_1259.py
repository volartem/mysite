# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-23 12:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visitor', '0012_auto_20170123_1248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visitor',
            name='image_url',
            field=models.SlugField(max_length=255),
        ),
    ]

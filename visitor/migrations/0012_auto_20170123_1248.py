# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-23 12:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('visitor', '0011_visitor_provider'),
    ]

    operations = [
        migrations.RenameField(
            model_name='visitor',
            old_name='user_img_url',
            new_name='image_url',
        ),
        migrations.RenameField(
            model_name='visitor',
            old_name='Uid',
            new_name='uid',
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-08 14:53
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0014_comment_parent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='parent',
        ),
        migrations.AddField(
            model_name='comment',
            name='path',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), null=True, size=None),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-08 15:26
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0015_auto_20170308_1453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='path',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), default=None, null=True, size=None),
        ),
    ]
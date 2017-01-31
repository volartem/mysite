# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-23 11:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('social_django', '0005_auto_20160727_2333'),
        ('visitor', '0004_remove_visitor_fuid'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='visitor',
            options={},
        ),
        migrations.AlterModelManagers(
            name='visitor',
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
        migrations.RemoveField(
            model_name='visitor',
            name='user_ptr',
        ),
        migrations.AddField(
            model_name='visitor',
            name='usersocialauth_ptr',
            field=models.OneToOneField(auto_created=True, default='', on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='social_django.UserSocialAuth'),
            preserve_default=False,
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-13 09:41
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.conf import settings
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=16)),
                ('text', models.TextField()),
                ('date_create', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('text', models.TextField()),
                ('date_create', models.DateTimeField(auto_now=True)),
                ('note', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='note.Note')),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='User', to=settings.AUTH_USER_MODEL)),
                ('path', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), blank=True, null=True, size=None)),
            ],
        ),
        migrations.AlterField(
            model_name='note',
            name='title',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='note',
            name='text',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='note',
            name='rubric',
            field=models.CharField(default='Other', max_length=255),
        ),
        migrations.CreateModel(
            name='Something',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('method', models.CharField(max_length=7)),
                ('path', models.CharField(max_length=255, verbose_name='Path')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('status_code', models.IntegerField(verbose_name='Status code')),
                ('ip', models.GenericIPAddressField()),
                ('refer', models.SlugField(default='not_refer', max_length=255, null=True)),
            ],
        ),
    ]

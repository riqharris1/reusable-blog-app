# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-30 10:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_tag'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='tag',
        ),
        migrations.RemoveField(
            model_name='post',
            name='views',
        ),
    ]
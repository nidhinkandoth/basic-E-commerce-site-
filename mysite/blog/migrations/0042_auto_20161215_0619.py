# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-15 06:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0041_auto_20161215_0600'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postssubmit',
            name='created_date',
        ),
        migrations.AddField(
            model_name='postssubmit',
            name='published_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]

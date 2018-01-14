# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-25 06:04
from __future__ import unicode_literals

from django.contrib.postgres.fields import JSONField
from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ('slack', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='membership',
            name='tz_count_json',
            field=JSONField(default={}),
        ),
    ]
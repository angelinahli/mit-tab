# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-02-26 19:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tab', '0002_auto_20180226_1925'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='judge',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='judge',
            name='provider',
        ),
    ]
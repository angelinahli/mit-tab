# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-02-27 01:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tab', '0005_merge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='judge',
            name='ballot_code',
            field=models.CharField(blank=True, max_length=256, null=True, unique=True),
        ),
    ]

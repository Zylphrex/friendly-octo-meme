# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-22 00:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faver_app', '0007_auto_20170122_0038'),
    ]

    operations = [
        migrations.AddField(
            model_name='faverrequest',
            name='reward',
            field=models.IntegerField(default=10),
        ),
        migrations.AlterField(
            model_name='faveruser',
            name='coins',
            field=models.IntegerField(default=5),
        ),
    ]

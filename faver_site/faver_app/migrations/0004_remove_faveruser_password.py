# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-22 00:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('faver_app', '0003_contract'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='faveruser',
            name='password',
        ),
    ]
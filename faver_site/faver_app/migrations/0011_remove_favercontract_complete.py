# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-22 07:45
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('faver_app', '0010_favercontract_complete'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='favercontract',
            name='complete',
        ),
    ]

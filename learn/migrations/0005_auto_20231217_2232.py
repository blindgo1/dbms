# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2023-12-17 22:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('learn', '0004_auto_20231217_2228'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='goods',
            name='sid',
        ),
        migrations.DeleteModel(
            name='supplier',
        ),
    ]

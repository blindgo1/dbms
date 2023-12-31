# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2023-12-17 22:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learn', '0005_auto_20231217_2232'),
    ]

    operations = [
        migrations.CreateModel(
            name='supplier',
            fields=[
                ('sid', models.IntegerField(primary_key=True, serialize=False)),
                ('sname', models.CharField(max_length=50, verbose_name='供应名称')),
                ('cname', models.CharField(max_length=50, verbose_name='联系人名称')),
                ('phone_num', models.CharField(max_length=50, verbose_name='电话')),
                ('email', models.CharField(max_length=50, verbose_name='邮箱')),
                ('address', models.CharField(max_length=50, verbose_name='地址')),
            ],
            options={
                'verbose_name': '供应商',
                'verbose_name_plural': '供应商',
                'db_table': 'supplier',
                'ordering': ['sid'],
            },
        ),
    ]

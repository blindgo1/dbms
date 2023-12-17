# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2021-01-04 21:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('learn', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('authorId', models.CharField(max_length=16, unique=True, verbose_name='作者账号')),
                ('authorName', models.CharField(max_length=5, verbose_name='姓名')),
                ('password', models.CharField(max_length=16, verbose_name='密码')),
                ('phone', models.CharField(max_length=11, unique=True, verbose_name='手机号')),
                ('age', models.IntegerField(null=True, verbose_name='年龄')),
                ('sex', models.CharField(choices=[('male', '男'), ('female', '女')], default='男', max_length=32, verbose_name='性别')),
                ('writing', models.CharField(max_length=11, null=True, verbose_name='写作时长')),
                ('content', models.TextField(null=True, verbose_name='写作信息')),
                ('c_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
            ],
            options={
                'verbose_name': '作者',
                'verbose_name_plural': '作者',
                'db_table': 'author',
                'ordering': ['c_time'],
            },
        ),
        migrations.CreateModel(
            name='Reader',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('readerId', models.CharField(max_length=16, unique=True, verbose_name='读者账号')),
                ('readerName', models.CharField(max_length=15, verbose_name='姓名')),
                ('password', models.CharField(max_length=16, verbose_name='密码')),
                ('phone', models.CharField(max_length=11, unique=True, verbose_name='手机号')),
                ('age', models.IntegerField(null=True, verbose_name='年龄')),
                ('sex', models.CharField(choices=[('male', '男'), ('female', '女')], default='男', max_length=32, verbose_name='性别')),
                ('feedback', models.TextField(null=True, verbose_name='反馈')),
                ('c_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('subscribe', models.ManyToManyField(blank=True, to='learn.Learn', verbose_name='订阅小说')),
            ],
            options={
                'verbose_name': '读者',
                'verbose_name_plural': '读者',
                'db_table': 'reader',
                'ordering': ['c_time'],
            },
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2021-03-01 11:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Academic', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vedio',
            name='url',
            field=models.URLField(default='www.tfswufe.edu.cn', verbose_name='直播地址'),
        ),
    ]

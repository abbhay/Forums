# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2021-03-01 11:45
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20210301_1059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailverfiy',
            name='send_time',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='发送时间'),
        ),
    ]
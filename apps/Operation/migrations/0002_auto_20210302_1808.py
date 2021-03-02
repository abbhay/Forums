# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2021-03-02 18:08
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Operation', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userbaoming',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='报名时间'),
        ),
        migrations.AlterField(
            model_name='userfavorites',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='收藏时间'),
        ),
        migrations.AlterField(
            model_name='usermessages',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='发送时间'),
        ),
        migrations.AlterField(
            model_name='userxueshu',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='发送时间'),
        ),
        migrations.AlterField(
            model_name='xueshucomments',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='评论时间'),
        ),
    ]
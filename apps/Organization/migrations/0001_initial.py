# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2020-09-03 16:02
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='category_org',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('org_category', models.CharField(max_length=20, verbose_name='机构/大学学校类型')),
                ('desc', models.CharField(max_length=100, verbose_name='描述')),
                ('add_time', models.DateField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '机构类型',
                'verbose_name_plural': '机构类型',
            },
        ),
        migrations.CreateModel(
            name='reporters',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, verbose_name='学术报告人姓名')),
                ('title', models.CharField(max_length=50, verbose_name='学术报告人的职称')),
                ('teacher_image', models.ImageField(upload_to='teacher/%Y/%m', verbose_name='机构/大学学校logo')),
                ('bithday', models.DateField(blank=True, null=True, verbose_name='生日')),
                ('personal_webinfo', models.URLField(blank=True, null=True, verbose_name='网址个人博客等等')),
                ('infomation', models.CharField(max_length=200, verbose_name='学术报告人的简介')),
                ('gender', models.CharField(choices=[('male', '男'), ('female', '女')], max_length=2, verbose_name='性别')),
                ('mobile', models.CharField(blank=True, max_length=11, null=True, verbose_name='手机号')),
                ('add_time', models.DateField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '报告人信息',
                'verbose_name_plural': '报告人信息',
            },
        ),
        migrations.CreateModel(
            name='XueshuOrg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('org_name', models.CharField(max_length=50, verbose_name='机构/大学学校名字')),
                ('org_desc', models.CharField(max_length=200, verbose_name='机构/大学学校名字')),
                ('org_address', models.CharField(max_length=100, verbose_name='机构/大学学校位置')),
                ('org_image', models.ImageField(upload_to='org/%Y/%m', verbose_name='机构/大学学校logo')),
                ('click_nums', models.IntegerField(default=0, verbose_name='点击数')),
                ('fav_nums', models.IntegerField(default=0, verbose_name='收藏数')),
                ('add_time', models.DateField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('org_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Organization.category_org', verbose_name='机构/大学学校类别')),
            ],
            options={
                'verbose_name': '组织机构信息',
                'verbose_name_plural': '组织机构信息',
            },
        ),
        migrations.AddField(
            model_name='reporters',
            name='org_teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Organization.XueshuOrg', verbose_name='组织'),
        ),
    ]

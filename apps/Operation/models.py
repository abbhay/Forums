from datetime import datetime

from django.db import models
from users.models import UserProfile
from Academic.models import Xueshu
# Create your models here.



class XueShuComments(models.Model):
    user = models.ForeignKey(UserProfile,verbose_name='评论用户',on_delete=models.CASCADE)
    xueshu  = models.ForeignKey(Xueshu,verbose_name='学报期数',on_delete=models.CASCADE)
    comments = models.CharField(max_length=200,verbose_name='评论')
    add_time = models.DateField(default=datetime.now,verbose_name='评论时间')

    class Meta:
        verbose_name = '学术评论'
        verbose_name_plural = verbose_name

class UserFavorites(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name='用户',on_delete=models.CASCADE)
    fav_id = models.IntegerField(default=0,verbose_name='数据id')
    fav_type = models.IntegerField(choices=((1,'学术'),(2,'机构'),(3,'报告人')),verbose_name='数据id',default=1)
    add_time = models.DateField(default=datetime.now, verbose_name='收藏时间')

    class Meta:
        verbose_name = '用户收藏'
        verbose_name_plural = verbose_name

class UserMessages(models.Model):
    user = models.IntegerField(default=0,verbose_name='接受用户')
    message = models.CharField(max_length=500,verbose_name='消息')
    has_read = models.BooleanField(default=False,verbose_name="是否已读")
    add_time = models.DateField(default=datetime.now, verbose_name='发送时间')

    class Meta:
        verbose_name = '用户消息'
        verbose_name_plural = verbose_name


class UserXueshu(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name='评论用户',on_delete=models.CASCADE)
    xueshu = models.ForeignKey(Xueshu, verbose_name='学报期数',on_delete=models.CASCADE)
    add_time = models.DateField(default=datetime.now, verbose_name='发送时间')

    class Meta:
        verbose_name = '用户消息'
        verbose_name_plural = verbose_name

class UserBaoming(models.Model):
    name = models.CharField(max_length=20,verbose_name='姓名')
    xuehao = models.CharField(max_length=8,verbose_name=u'学号')
    mobile = models.CharField(max_length=11, verbose_name=u'手机号', null=True, blank=True)
    add_time = models.DateField(default=datetime.now, verbose_name='报名时间')

    class Meta:
        verbose_name = '用户报名'
        verbose_name_plural = verbose_name
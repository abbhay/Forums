from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class UserProfile(AbstractUser):
    xuehao = models.CharField(max_length=8,verbose_name=u'学号',unique=True)
    gender = models.CharField(choices=(('male',u"男"),('female',u"女")),max_length=2,verbose_name=u'性别')
    bithday = models.DateField(verbose_name=u'生日',null=True,blank=True)
    mobile = models.CharField(max_length=11,verbose_name=u'手机号',null=True,blank=True)
    classes = models.CharField(max_length=6,verbose_name=u"班级")
    bedroom = models.CharField(max_length=10,verbose_name=u'寝室号',null=True,blank=True)
    school_department = models.CharField(max_length=20,verbose_name='学院',default=u"智能科技学院")
    counselor = models.CharField(max_length=8,verbose_name=u"辅导员",null=True,blank=True)
    quality_score = models.FloatField(verbose_name='素质拓展分',default=0.0)
    weights = models.FloatField(verbose_name=u'权重',default=0.0)
    watch_time = models.IntegerField(verbose_name=u'观看学报次数',default=0)
    school_position = models.CharField(max_length=20,verbose_name=u"校区")
    image = models.ImageField(upload_to="image/%Y/%m",default=u"image/default.png",max_length=100)

    class Meta:
        verbose_name = u'用户信息'
        verbose_name_plural =  verbose_name

    def __str__(self):
        return self.username


class EmailVerfiy(models.Model):
    code = models.CharField(max_length=20,verbose_name='验证码')
    email = models.CharField(max_length=50,verbose_name='邮箱地址')
    send_type = models.CharField(choices=(('register','注册'),('forget','找回密码')),max_length=10)
    send_time = models.DateField(default=datetime.now,verbose_name='发送时间')

    class Meta:
        verbose_name = u'邮箱信息'
        verbose_name_plural =  verbose_name

class Banner(models.Model):
    title = models.CharField(max_length=50,verbose_name='标题')
    image = models.ImageField(upload_to='banner/%Y/%m',max_length=100,verbose_name="banner图片地址")
    url = models.URLField(max_length=100,verbose_name="跳转地址")
    inde = models.IntegerField(default=100,verbose_name='顺序')
    add_time =  models.DateField(default=datetime.now,verbose_name='添加时间')

    class Meta:
        verbose_name = '轮播图'
        verbose_name_plural = verbose_name

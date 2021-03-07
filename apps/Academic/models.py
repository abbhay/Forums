from datetime import datetime

from django.db import models
from Organization.models import XueshuOrg
from utils.utils import return_category
# Create your models here.

class Xueshu(models.Model):
    xueshu_orgs = models.ForeignKey(XueshuOrg, verbose_name='学术机构',default='', on_delete=models.CASCADE)
    title = models.CharField(max_length=50,verbose_name='标题',)
    desc = models.CharField(max_length=200,verbose_name='描述')
    url = models.URLField(verbose_name='官网的展示网页')
    category  = models.CharField(choices=return_category(),max_length=2,verbose_name='种类')
    learn_time = models.IntegerField(default=150,verbose_name='举办时长/分钟')
    hold_place = models.CharField(default='绵阳学术报告厅',verbose_name='举办地点',max_length=50)
    student = models.IntegerField(default=0,verbose_name='报名人数')#优先显示好友位
    fav_id = models.IntegerField(default=0,verbose_name="收藏数")
    click_num = models.IntegerField(default=0,verbose_name="点击数")
    image = models.ImageField(upload_to="xueshu/%Y/%m", default=u"image/default.png", max_length=100)
    add_time = models.DateField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = u'学术信息'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.title

    def get_users(self):
        return self.userxueshu_set.all()[:3]
    def get_vedio(self):
        return self.vedio_set.all()

class Vedio(models.Model):
    Xueshu = models.ForeignKey(Xueshu,verbose_name='学术报告',on_delete=models.CASCADE)
    name = models.CharField(max_length=20,verbose_name='名称')
    url = models.URLField(verbose_name='直播地址',default='www.tfswufe.edu.cn')
    add_time = models.DateField(default=datetime.now,verbose_name='添加时间')

    class Meta:
        verbose_name = u'直播回放视频'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.name

class Resource(models.Model):
    Xueshu = models.ForeignKey(Xueshu, verbose_name='学术报告',on_delete=models.CASCADE)
    name = models.CharField(max_length=20, verbose_name='名称')
    download = models.FileField(upload_to='Xueshu/%Y/%m',verbose_name="资源文件",max_length=200)
    add_time = models.DateField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = u'学术资源'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.name

from datetime import datetime

from django.db import models

# Create your models here.

class category_org(models.Model):
    org_category = models.CharField(max_length=20,verbose_name='机构/大学学校类型')
    desc = models.CharField(max_length=100,verbose_name='描述')
    add_time = models.DateField(default=datetime.now,verbose_name='添加时间')

    class Meta:
        verbose_name = u'机构类型'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.org_category


class XueshuOrg(models.Model):
    org_category = models.ForeignKey(category_org,verbose_name='机构/大学学校类别',on_delete=models.CASCADE)
    org_name = models.CharField(max_length=50,verbose_name='机构/大学学校名字')
    org_desc = models.CharField(max_length=200,verbose_name='机构/大学学校描述')
    url = models.URLField(verbose_name="机构/大学学校网址",default="www.baidu.com")
    org_address = models.CharField(max_length=100,verbose_name='机构/大学学校位置')
    org_image = models.ImageField(upload_to='org/%Y/%m',verbose_name='机构/大学学校logo',max_length=100)
    click_nums = models.IntegerField(default=0,verbose_name='点击数')
    fav_nums = models.IntegerField(default=0,verbose_name='收藏数')
    students = models.IntegerField(default=0,verbose_name='学习人数')
    add_time = models.DateField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = u'组织机构信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.org_name


class reporters(models.Model):
    org_teacher = models.ForeignKey(XueshuOrg, verbose_name='组织',on_delete=models.CASCADE)
    name = models.CharField(max_length=10,verbose_name='学术报告人姓名')
    title = models.CharField(max_length=50,verbose_name='学术报告人的简介')
    teacher_image = models.ImageField(upload_to='teacher/%Y/%m', verbose_name='老师的照片', max_length=100)
    bithday = models.DateField(verbose_name=u'生日',null=True,blank=True)
    personal_webinfo = models.URLField(verbose_name=u'网址个人博客等等',blank=True)
    infomation = models.CharField(max_length=200,verbose_name='学术报告人的简介')
    gender = models.CharField(choices=(('male', u"男"), ('female', u"女")), max_length=8, verbose_name=u'性别')
    mobile = models.CharField(max_length=11, verbose_name=u'手机号', null=True, blank=True)
    add_time = models.DateField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = u'报告人信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


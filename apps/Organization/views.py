from django.http import HttpResponse
from django.shortcuts import render
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.
from django.views.generic.base import View
from .models import XueshuOrg,category_org
from .forms import UserBaomingForm

class OrgView(View):
    """
    课程机构列表功能
    """
    def get(self, request):

        #课程机构
        all_orgs = XueshuOrg.objects.all()
        hot_orgs = all_orgs.order_by("-click_nums")[:3]


        all_category = category_org.objects.all()
        # 取出筛选城市
        city_id = request.GET.get('city', "")

        if city_id:
            all_orgs = all_orgs.filter(id=int(city_id))

        # 取出类别筛选
        category = request.GET.get('ct', "")
        if category:
            all_orgs = all_orgs.filter(org_category_id=int(category))

        # 学习人数筛选
        sort = request.GET.get('sort', "")
        if sort:
            if sort=='students':
                all_orgs = all_orgs.order_by("-students")
                print("111")
            elif sort=='time':
                all_orgs=all_orgs.order_by("-add_time")

        # 对课程机构进行分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(all_orgs, 2, request=request)

        orgs = p.page(page)

        org_nums = all_orgs.count()
        return render(request, "org-list.html", {
            "all_orgs":orgs,
            "all_citys":all_category,
            'org_nums':org_nums,
            'city_id':city_id,
            'category':category,
            'hot_orgs':hot_orgs

        })



class AddUserBaomingView(View):
    """
    用户添加咨询
    """
    def post(self, request):
        userask_form = UserBaomingForm(request.POST)
        if userask_form.is_valid():
            user_ask = userask_form.save(commit=True)
            return HttpResponse('{"status":"success"}', content_type='application/json')
        else:
            return HttpResponse('{"status":"fail", "msg":"添加出错"}', content_type='application/json')
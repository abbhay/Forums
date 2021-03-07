from django.http import HttpResponse
from django.shortcuts import render
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.
from django.views.generic.base import View
from .models import XueshuOrg,category_org,reporters
from .forms import UserBaomingForm
from Operation.models import UserFavorites
from Academic.models import Xueshu

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

class OrgHomeView(View):
    """
    机构首页
    """
    def get(self, request, org_id):
        current_page = "home"
        xueshu_org = XueshuOrg.objects.get(id=int(org_id))
        all_xueshu = xueshu_org.xueshu_set.all()
        all_teachers = xueshu_org.reporters_set.all()[:2]
        xueshu_org.click_nums += 1
        xueshu_org.save()
        has_fav = False
        print(xueshu_org.id)
        # if request.user.is_authenticated():
        #     if UserFavorite.objects.filter(user=request.user, fav_id=course_org.id, fav_type=2):
        #         has_fav = True
        return render(request, 'org-detail-homepage.html', {
            'all_courses':all_xueshu,
            'all_teachers': all_teachers,
            'xueshu_org':xueshu_org,
            'current_page':current_page,
            'has_fav':has_fav
        })


class OrgXueshuView(View):

    def get(self, request, org_id):
        current_page = "xueshu"
        xueshu_org = XueshuOrg.objects.get(id=int(org_id))
        #
        # has_fav = False
        # # if request.user.is_authenticated():
        # #     if UserFavorite.objects.filter(user=request.user, fav_id=course_org.id, fav_type=2):
        # #         has_fav = True
        all_xueshus = xueshu_org.xueshu_set.all()
        return render(request, 'org-detail-course.html', {
            'all_xueshus':all_xueshus,
            'xueshu_org':xueshu_org,
            'current_page':current_page,
            # 'has_fav':has_fav
        })

class OrgDescView(View):
    """
    机构介绍页
    """
    def get(self, request, org_id):
        current_page = "desc"
        xueshu_org = XueshuOrg.objects.get(id=int(org_id))
        # has_fav = False
        # if request.user.is_authenticated():
        #     if UserFavorite.objects.filter(user=request.user, fav_id=course_org.id, fav_type=2):
        #         has_fav = True
        return render(request, 'org-detail-desc.html', {
            'xueshu_org':xueshu_org,
            'current_page':current_page,
        })


class OrgTeacherView(View):
    """
    机构教师页
    """
    def get(self, request, org_id):
        current_page = "teacher"
        xueshu_org = XueshuOrg.objects.get(id=int(org_id))
        has_fav = False
        # if request.user.is_authenticated():
        #     if UserFavorite.objects.filter(user=request.user, fav_id=course_org.id, fav_type=2):
        #         has_fav = True
        all_teachers = xueshu_org.reporters_set.all()
        return render(request, 'org-detail-teachers.html', {
            'all_teachers':all_teachers,
            'xueshu_org':xueshu_org,
            'current_page':current_page,


        })



class AddFavView(View):
    """
    用户收藏，用户取消收藏
    """
    def post(self, request):
        fav_id = request.POST.get('fav_id', 0)
        fav_type = request.POST.get('fav_type', 0)

        if not request.user.is_authenticated():
            #判断用户登录状态
            return HttpResponse('{"status":"fail", "msg":"用户未登录"}', content_type='application/json')

        exist_records = UserFavorites.objects.filter(user=request.user, fav_id=int(fav_id), fav_type=int(fav_type))

        if exist_records:
            #如果记录已经存在， 则表示用户取消收藏
            exist_records.delete()
            if int(fav_type) == 1:
                course = Xueshu.objects.get(id=int(fav_id))
                course.fav_id -= 1
                if course.fav_id < 0:
                    course.fav_id = 0
                course.save()
            elif int(fav_type) == 2:
                course_org = XueshuOrg.objects.get(id=int(fav_id))
                course_org.fav_nums -= 1
                if course_org.fav_nums < 0:
                    course_org.fav_nums = 0
                course_org.save()
            # elif int(fav_type) == 3:
            #     teacher = reporters.objects.get(id=int(fav_id))
            #     teacher.fav_nums -= 1
            #     if teacher.fav_nums < 0:
            #         teacher.fav_nums = 0
            #     teacher.save()
            return HttpResponse('{"status":"success", "msg":"收藏"}', content_type='application/json')
        else:
            user_fav = UserFavorites()
            if int(fav_id) > 0 and int(fav_type) > 0:
                user_fav.user = request.user
                user_fav.fav_id = int(fav_id)
                user_fav.fav_type = int(fav_type)
                user_fav.save()

                if int(fav_type) == 1:
                    course = Xueshu.objects.get(id=int(fav_id))
                    course.fav_id += 1
                    course.save()
                elif int(fav_type) == 2:
                    course_org = XueshuOrg.objects.get(id=int(fav_id))
                    course_org.fav_nums += 1
                    course_org.save()
                elif int(fav_type) == 3:
                    teacher = reporters.objects.get(id=int(fav_id))
                    teacher.fav_nums += 1
                    teacher.save()

                return HttpResponse('{"status":"success", "msg":"已收藏"}', content_type='application/json')
            else:
                return HttpResponse('{"status":"fail", "msg":"收藏出错"}', content_type='application/json')
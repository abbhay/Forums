from django.shortcuts import render
from django.views.generic.base import View
from .models import Xueshu,Resource
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.
from utils.mixin_utils import LoginRequiredMixin
from Operation.models import UserFavorites,UserXueshu
class XueshuListView(View):
    def get(self, request):
        all_xueshu = Xueshu.objects.all().order_by("-add_time")
        # #课程搜索
        # search_keywords = request.GET.get('keywords', "")
        # if search_keywords:
        #     all_courses = all_courses.filter(Q(name__icontains=search_keywords)|Q(desc__icontains=search_keywords)|Q(detail__icontains=search_keywords))
        #
        #课程排序
        sort = request.GET.get('sort', "")
        if sort:
            if sort == "students":
                all_xueshu = all_xueshu.order_by("-student")
            elif sort == "hot":
                all_xueshu = all_xueshu.order_by("-click_num")

        #对课程进行分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(all_xueshu, 3, request=request)

        all_xueshu = p.page(page)


        return render(request, 'course-list.html', {
            "all_xueshus":all_xueshu
            # "sort":sort,
            # "hot_courses":hot_courses
        })



class XueshuDetailView(View):

    def get(self, request, course_id):
        xueshus = Xueshu.objects.get(id=int(course_id))
        #
        #增加课程点击数
        xueshus.click_num += 1
        xueshus.save()
        #
        #是否收藏课程
        has_fav_course = False
        #是否收藏机构
        has_fav_org = False
        print(request.user.is_authenticated())

        if request.user.is_authenticated():
            if UserFavorites.objects.filter(user=request.user, fav_id=xueshus.id, fav_type=1):
                has_fav_course = True

            if UserFavorites.objects.filter(user=request.user, fav_id=xueshus.xueshu_orgs.id, fav_type=2):
                has_fav_org = True


        return render(request, "course-detail.html", {
            "xueshus":xueshus,
            "has_fav_course":has_fav_course,
            "has_fav_org":has_fav_org
        })

class XueshuInfoView(LoginRequiredMixin, View):
    """
    课程章节信息
    """
    def get(self, request, course_id):
        course = Xueshu.objects.get(id=int(course_id))
        course.student += 1
        course.save()
        # #查询用户是否已经关联了该课程
        # user_courses = UserXueshu.objects.filter(user=request.user, course=course)
        # if not user_courses:
        #     user_course = UserXueshu(user=request.user, course=course)
        #     user_course.save()
        #
        # user_cousers = UserXueshu.objects.filter(course=course)
        # user_ids = [user_couser.user.id for user_couser in user_cousers]
        # all_user_courses = UserXueshu.objects.filter(user_id__in=user_ids)
        # #取出所有课程id
        # course_ids = [user_couser.course.id for user_couser in all_user_courses]
        # #获取学过该用户学过其他的所有课程
        # relate_courses = Xueshu.objects.filter(id__in=course_ids).order_by("-click_nums")[:5]
        # all_resources = Resource.objects.filter(course=course)
        return render(request, "course-video.html", {
            "course":course,
            # "course_resources":all_resources,
            # "relate_courses":relate_courses
        })
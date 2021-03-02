import  json

from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.contrib.auth.hashers import make_password
from .forms import LoginForm,RegisterForm
from .models import UserProfile,EmailVerfiy
from django.views.generic.base import View
from Operation.models import  UserMessages
from utils.email_send import send_register_email
# Create your views here.
class CustomBackend(ModelBackend):
    def authenticate(self, username=None, password=None, **kwargs):
        try:
            user = UserProfile.objects.get(Q(username=username)|Q(email=username))
            print("aaaa")
            if user.check_password(password):
                return user
        except Exception as e:
            return None


class LoginView(View):
    def get(self, request):
        return render(request, "login.html", {})
    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_name = request.POST.get("username", "")
            pass_word = request.POST.get("password", "")
            user = authenticate(username=user_name, password=pass_word)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(reverse("index"))
                else:
                    return render(request, "login.html", {"msg":"用户未激活！"})
            else:
                return render(request, "login.html", {"msg":"用户名或密码错误！"})
        else:
            return render(request, "login.html", {"login_form":login_form})


# class ResetView(View):
#     def get(self, request, active_code):
#         all_records = EmailVerifyRecord.objects.filter(code=active_code)
#         if all_records:
#             for record in all_records:
#                 email = record.email
#                 return render(request, "password_reset.html", {"email":email})
#         else:
#             return render(request, "active_fail.html")
#         return render(request, "login.html")

class RegisterView(View):
    def get(self, request):
        register_form = RegisterForm()
        return render(request, "register.html", {'register_form':register_form})

    def post(self, request):
        register_form = RegisterForm(request.POST)
        print(register_form)
        if register_form.is_valid():
            user_name = request.POST.get("email", "")
            if UserProfile.objects.filter(email=user_name):
                return render(request, "register.html", {"register_form":register_form, "msg":"用户已经存在"})
            pass_word = request.POST.get("password", "")
            user_profile = UserProfile()
            user_profile.username = user_name
            user_profile.email = user_name
            user_profile.is_active = False
            user_profile.password = make_password(pass_word)
            user_profile.save()

            #写入欢迎注册消息
            user_message = UserMessages()
            user_message.user = user_profile.id
            user_message.message = "欢迎注册智能论坛在线网"
            user_message.save()

            send_register_email(user_name, "register")
            print("11111")
            return render(request, "login.html")
        else:
            return render(request, "register.html", {"register_form":register_form})

class AciveUserView(View):
    def get(self, request, active_code):
        all_records = EmailVerfiy.objects.filter(code=active_code)
        if all_records:
            for record in all_records:
                email = record.email
                user = UserProfile.objects.get(email=email)
                user.is_active = True
                user.save()
        else:
            return render(request, "active_fail.html")
        return render(request, "login.html")

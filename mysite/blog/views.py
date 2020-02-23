from django.shortcuts import render, HttpResponse, render_to_response, redirect
import time
# Create your views here.
from blog.models import *


def show_time(req):
    t = time.ctime()
    return render_to_response('index.html',{"t":t})
    # return render(req, "index.html", {'t': t})
    # return HttpResponse("hello")


def article_year(request, year, month):
    return HttpResponse("year:%s, month:%s" % (year, month))


def re_test(req, num):
    return HttpResponse("这是用正则匹配到的！:%s" % num)


def register(req):
    if req.method == "POST":
        print(req.POST.get("user"))
        name = req.POST.get("user")
        return redirect('/blog/login/')
        # return render(req, 'login.html', locals())
    return render(req, 'register.html')


def login(req):
    return HttpResponse('login.html')


def index(req):
    return render(req, 'index.html')


def addbook(req):
    b = Book(name='python', price=99, pub_data="2020-02-23")
    b.save()
    return HttpResponse("添加成功")

import time

from django.shortcuts import render, HttpResponse, redirect


def index(request):
    return HttpResponse('Hello Django')


def rebad(request):
    # redirect('The link what you want to jump')
    return redirect('http://www.baidu.com')


def now_time(request):
    now_time = time.strftime('%Y-%m-%d %X', time.localtime())
    # render(request, "name.html", {The value you want render})
    return render(request, "now_time.html", {'now_time': now_time})
# Create your views here.

from django import http
from django.shortcuts import render, redirect

from goods.models import GoodsCategory


def login_with_cookie(request):
    if request.method == 'GET':
        uid = request.COOKIES.get('uid')
        if not uid:
            return render(request, 'demo/login.html')
        else:
            return render(request, 'demo/home.html', {'uid': uid})
    else:
        uid = request.POST.get('uid')
        response = redirect('login_with_cookie')
        response.set_cookie('uid', uid)
        return response


def login_with_session(request):
    if request.method == 'GET':
        uid = request.session.get('uid')
        if not uid:
            return render(request, 'demo/login.html')
        else:
            return render(request, 'demo/home.html', {'uid': uid})
    else:
        uid = request.POST.get('uid')
        request.session['uid'] = uid
        return redirect('login_with_session')


def recursion(request):
    cat1_list = GoodsCategory.objects.filter(parent__isnull=True)
    return render(request, 'demo/recursion.html', {'cat1_list': cat1_list})

from django import http
from django.shortcuts import render, redirect


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

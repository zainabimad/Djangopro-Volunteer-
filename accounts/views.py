from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import login,authenticate,logout
# Create your views here.


def login_as(request):
    if request.method =='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user :
           login(request,user)
           msg="تم تسجيل الدخول"
           return render(request, 'Index.html', {'msg': msg})
        else:
            return HttpResponse('error')
    return render(request,'Login.html')
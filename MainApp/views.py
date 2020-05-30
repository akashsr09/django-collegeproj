from django.shortcuts import render
from django.http import HttpResponse
from .models import Register
from . import models

k=[]
# Create your views here.
def index(request):
    return render(request,'MainApp/index.html')
def register(request):
    return render(request, 'MainApp/register.html')
def login(request):
    return render(request, 'MainApp/login.html')
def reg_done(request):
    a=Register()
    a.name=request.POST.get('name')
    a.mail=request.POST.get('email')
    a.phone=request.POST.get('phone')
    a.psw=request.POST.get('pwd')
    a.pswr=request.POST.get('rpwd')
    a.save()
    k.append(a)
    return render(request, 'MainApp/reg_done.html',{'all':k})
def sorry(request):
    return render(request, 'MainApp/sorry.html')
def login_done(request):

    lpwd=request.POST.get('lpwd')
    lmail=request.POST.get('lmail')
    for i in k:
        if i[1]==lmail and i[3]==lpwd:
            return render(request, 'MainApp/login_done.html')
        else:
            return render(request, 'MainApp/sorry.html')
    return render(request, 'MainApp/login_done.html')

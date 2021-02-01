from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def fun1(req):
    return render(req,'ass1.html')
def fun2(req):
    return render(req,'ass2.html')
def fun3(req):
    return render(req,'ass3.html')   
def fun4(req):
    return render(req,'ass4.html')
def fun5(req):
     return render(req,'ass5.html')
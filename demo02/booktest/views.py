from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    print(request)
    return HttpResponse("首页")


def list(request):
    print(request)
    return HttpResponse("列表")

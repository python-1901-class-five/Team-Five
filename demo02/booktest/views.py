from django.shortcuts import render
from django.http import HttpResponse
from .models import Bookinfo, Heroinfo
from django.template import loader, RequestContext
# Create your views here.


def index(request):
    # 加载模板
    # template = loader.get_template('booktest/index.html')
    context = {}
    # res = template.render(context=context)
    # return HttpResponse(res)
    return render(request, 'booktest/index.html', context)


def list(request):
    # list1 = []
    # for i in Bookinfo.objects.all():
    #     print(i, type(i))
    #     list1.append(i)
    # return HttpResponse(list1)
    # template = loader.get_template('booktest/list.html')
    booklist = Bookinfo.objects.all()
    context = {'booklist':booklist}
    # res = template.render(context=context)
    # return HttpResponse(res)
    return render(request, 'booktest/list.html', context)


def detail(request, id):
    book = Bookinfo.objects.get(pk=int(id))
    context = {'book': book}
    # return HttpResponse(book)
    return render(request, 'booktest/detail.html', context)

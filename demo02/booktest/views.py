from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from .models import Bookinfo, Heroinfo
from django.template import loader, RequestContext
# Create your views here.
from django.urls import reverse


def index(request):
    # 加载模板
    # template = loader.get_template('booktest/index.html')
    username = request.session.get('username')
    context = {"username": username}
    # res = template.render(context=context)
    # return HttpResponse(res)
    return render(request, 'booktest/index.html', context)


def login(request):
    return render(request, 'booktest/login.html')


def loginhandler(request):
    username = request.POST['username']
    request.session['username'] = username
    return redirect(reverse('booktest:index'))
    # return render(request, 'booktest/index.html', {'username': username})


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


def delete(request, id):
    Bookinfo.objects.get(pk=int(id)).delete()
    booklist = Bookinfo.objects.all()
    return render(request, 'booktest/list.html', {'booklist':booklist})


def add(request):
    # return render(request, 'booktest/addbook.html', {})
    return render(request, 'booktest/addbook.html')


def addbook(request):
    b1 = Bookinfo()
    b1.btitle = request.POST['btitle']
    b1.save()
    booklist = Bookinfo.objects.all()
    # return render(request, 'booktest/list.html', {'booklist': booklist})
    return HttpResponseRedirect('/booktest/list/', {'booklist': booklist})
    # return HttpResponse("添加成功")


def addhero(request, id):
    return render(request, 'booktest/addhero.html', {'bookid': id})
    # return HttpResponse("添加成功")


def addherohandler(request):
    bookid = request.POST["bookid"]
    hname = request.POST["hname"]
    hgender = request.POST["hgender"]
    hcontent = request.POST["hcontent"]
    print(bookid, hname, hgender, hcontent)
    book = Bookinfo.objects.get(pk=int(bookid))
    hero = Heroinfo()
    hero.hname = hname
    if hgender == 1:
        hero.hgender = True
    else:
        hero.hgender = False
    hero.hcontent = hcontent
    hero.hbook = book
    hero.save()
    return HttpResponseRedirect('/booktest/detail/'+str(bookid)+"/", {'book': book})

from django.shortcuts import *
# Create your views here.
from .models import Bookinfo


def index(request):
    # 运用render方法
    # return render(request, 'test2/test.html')
    # 运用redirect方法
    # return redirect('/test2/list/')
    # 运用redirect+reverse方法
    return redirect(reverse('test2:list1'))


def list1(request):
    book = Bookinfo.objects.all()
    return render(request, 'test2/test.html', {'book': book})


def detail(request,id):
    # try:
    #     book = get_object_or_404(Bookinfo, pk=id)
    # except Exception:
    #     book = None
    # book = Bookinfo.objects.get(pk=id)
    # book = get_object_or_404(Bookinfo, pk=id)
    book = get_list_or_404(Bookinfo, pk__lt=1)
    return render(request, 'test2/detail.html', {'book': book})

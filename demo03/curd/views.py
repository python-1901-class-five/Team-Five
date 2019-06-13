from django.shortcuts import render
from .models import AreaInfo
# Create your views here.
def area(request):
    area = AreaInfo.objects.get(atitle='河南')
    return  render(request, 'curd/area.html',{'area':area})

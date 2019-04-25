from django import template
from ..models import Category, Tags ,Article

register = template.Library()


@register.simple_tag
def getcategory():
    cate = Category.objects.all()
    return cate


@register.simple_tag
def gettags():
    tags = Tags.objects.all()
    return tags


@register.simple_tag
def getlastest():
    return Article.objects.all().order_by('-create_time')[:3]


@register.simple_tag
def gettime():
    return Article.objects.dates('create_time','month',order='DESC')[:3]

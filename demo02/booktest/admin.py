from django.contrib import admin
from .models import Bookinfo, Heroinfo
# Register your models here.


class Heroinfoinline(admin.StackedInline):
    model = Heroinfo
    extra = 1


class BookinfoAdmin(admin.ModelAdmin):
    list_display = ["title", "createtime"]
    list_filter = ['btitle']
    search_fields = ['btitle']
    list_per_page = 2
    inlines = [Heroinfoinline]


class HeroinfoAdmin(admin.ModelAdmin):
    list_display = ['name', 'gender', 'skill', 'include']
    list_filter = ['hname', 'hgender']
    search_fields = ['hname', 'hgender', 'hcontent']
    list_per_page = 3


admin.site.register(Bookinfo, BookinfoAdmin)
admin.site.register(Heroinfo, HeroinfoAdmin)

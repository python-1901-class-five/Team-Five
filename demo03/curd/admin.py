from django.contrib import admin
from .models import Account, Contact, Aplication, Host, Heroinfo, Bookinfo,AreaInfo
# Register your models here.
admin.site.register(Account)
admin.site.register(Contact)
admin.site.register(Aplication)
admin.site.register(Host)
admin.site.register(Heroinfo)
admin.site.register(Bookinfo)
admin.site.register(AreaInfo)
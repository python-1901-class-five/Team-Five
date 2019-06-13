from django.contrib import admin
from .models import Article, Classify, Comment, Label
# Register your models here.
admin.site.register(Article)
admin.site.register(Comment)
admin.site.register(Classify)
admin.site.register(Label)
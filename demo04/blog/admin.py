from django.contrib import admin
from .models import Article, Comment, Category, Tags
# Register your models here.

admin.site.register(Article)
admin.site.register(Comment)
admin.site.register(Category)
admin.site.register(Tags)
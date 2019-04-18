from django.contrib import admin
from .models import Question, Choice

# Register your models here.


class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 1


class QuestionAdmin(admin.ModelAdmin):
    list_display = ['qname', 'createtime']
    list_filter = ['qtitle']
    search_fields = ['qtitle']
    list_per_page = 3
    inlines = [ChoiceInline]


class ChoiceAdmin(admin.ModelAdmin):
    list_display = ['choicename', 'countnum']
    list_filter = ['cname']
    search_fields = ['cname']
    list_per_page = 2


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)

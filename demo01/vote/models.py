from django.db import models

# Create your models here.


class Question(models.Model):
    qtitle = models.CharField(max_length=50)
    qtime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.qtitle

    def qname(self):
        return self.qtitle
    qname.short_description = '问题'

    def createtime(self):
        return self.qtime
    createtime.short_description = '创建时间'


class Choice(models.Model):
    cname = models.CharField(max_length=10)
    ccount = models.IntegerField()
    cques = models.ForeignKey('Question', on_delete=models.CASCADE)

    def __str__(self):
        return self.cname

    def choicename(self):
        return self.cname
    choicename.short_description = '选择'

    def countnum(self):
        return self.ccount
    countnum.short_description = '投票数'
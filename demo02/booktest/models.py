from django.db import models

# Create your models here.


class Bookinfo(models.Model):
    btitle = models.CharField(max_length=20)
    bpub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%d:%s" % (self.pk, self.btitle)

    def title(self):
        return self.btitle

    title.short_description = '书名'

    def createtime(self):
        return self.bpub_date

    createtime.short_description = '创建时间'


class Heroinfo(models.Model):
    hname = models.CharField(max_length=20)
    hgender = models.BooleanField()
    hcontent = models.CharField(max_length=100)
    hbook = models.ForeignKey('Bookinfo', on_delete=models.CASCADE)

    def __str__(self):
        return "%d:%s" % (self.pk, self.hname)

    def name(self):
        return self.hname

    name.short_description = '英雄名称'

    def gender(self):
        return self.hgender

    gender.short_description = '性别'

    def skill(self):
        return self.hcontent

    skill.short_description = '英雄技能'

    def include(self):
        return self.hbook

    include.short_description = '所属图书'

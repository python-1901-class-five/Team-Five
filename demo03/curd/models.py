from django.db import models

# Create your models here.


class Account(models.Model):
    username = models.CharField(max_length=20,null=True,blank=True,verbose_name='用户名')
    password = models.CharField(max_length=40,null=True,blank=True,verbose_name='密码')
    register_date = models.DateTimeField(auto_now_add=True,verbose_name='注册时间')


class Contact(models.Model):
    account = models.OneToOneField(Account, on_delete=models.CASCADE)
    address = models.CharField(max_length=20, null=True)
    code =models.CharField(max_length=20, null=True)
    mobile = models.CharField(max_length=20, null=True)


class Host(models.Model):
    hostname = models.CharField(max_length=32)
    ip = models.GenericIPAddressField(protocol='ipv4')
    port = models.IntegerField()


class Aplication(models.Model):
    name = models.CharField(max_length=32)
    h = models.ManyToManyField(to='Host')


class Bookinfo(models.Model):
    btitle = models.CharField(max_length=20)
    create_date = models.DateTimeField(auto_now_add=True)


class Heroinfo(models.Model):
    hname = models.CharField(max_length=20)
    hage = models.IntegerField(default=18)
    hcontent = models.CharField(max_length=40)
    hbook = models.ForeignKey('Bookinfo',on_delete=models.CASCADE)


# class Goods(models.Model):
#     name = models.CharField(max_length=20)
#     # mange = models.Manager()
#
#     @classmethod
#     def create(cls, _name):
#         goods = cls(name=_name)
#         return goods
class GoodsManage(models.Manager):
    # def create_book(self, name):
    #     goods = self.model()
    #     goods.name = name
    #     return goods

    def create_book(self, name):
        goods = self.create(name=name)
        return goods


class Goods(models.Model):
    name = models.CharField(max_length=20)
    mange = GoodsManage()


class AreaInfo(models.Model):
    atitle = models.CharField(max_length=20)
    aParent = models.ForeignKey('self', null=True, blank=True,on_delete=models.CASCADE)

    def __str__(self):
        return self.atitle

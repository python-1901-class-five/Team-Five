from django.db import models

# Create your models here.


class Classify(models.Model):
    fname = models.CharField(max_length=20)

    def __str__(self):
        return self.fname


class Article(models.Model):
    # 文章标题
    atitle = models.CharField(max_length=50)
    # 创建时间
    create_time = models.DateField(auto_now_add=True)
    # 作者
    author = models.CharField(max_length=20)
    # 阅读量
    read_count = models.IntegerField(default=0)
    # 摘要
    abstract = models.TextField()
    # 文本
    content = models.TextField()
    aclassify = models.ForeignKey('Classify', on_delete=models.CASCADE)

    def __str__(self):
        return self.atitle


class Comment(models.Model):
    cname = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.CharField(max_length=50)
    comcontent = models.TextField()
    carticle = models.ForeignKey('Article', on_delete=models.CASCADE)

    def __str__(self):
        return self.cname


class Label(models.Model):
    lname = models.CharField(max_length=20)
    larticle = models.ManyToManyField(to='Article')

    def __str__(self):
        return self.lname

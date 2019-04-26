from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Article(models.Model):
    atitle = models.CharField(max_length=50)
    create_time = models.DateField()
    read_count = models.IntegerField(default=0)
    abstract = models.TextField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    tags = models.ManyToManyField(to='Tags')

    def __str__(self):
        return self.atitle


class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Tags(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Comment(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    url = models.CharField(max_length=50)
    text = models.TextField()
    create_time = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('Article', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

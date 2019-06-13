from django.shortcuts import render
from .models import Article, Classify, Comment, Label
# Create your views here.


def index(request, i):
    article_all = Article.objects.all()
    articles = article_all[(int(i)-1)*4:(int(i)-1)*4+4]
    print(articles, articles[0].create_time.year)
    articles1 = article_all[len(article_all) - 3:len(article_all) + 1]
    l1 = []
    for art in article_all:
        l1.append(str(art.create_time.year)+' 年 '+str(art.create_time.month)+' 月')
    l2 = list(set(l1))
    l2.sort(key=l1.index)
    l3 = []
    for i in range(int(len(article_all)/4)+1):
        l3.append(str(i+1))
    classifies = Classify.objects.all()
    labels = Label.objects.all()
    comments = Comment.objects.all()
    context = {'articles': articles, 'article_all': article_all, 'articles1': articles1, 'date': l2, 'page':l3,'classifies': classifies, 'labels': labels, 'comments':comments}
    return render(request, 'blog/index.html', context)


def single(request, i):
    article_all = Article.objects.all()
    articles1 = article_all[len(article_all) - 3:len(article_all) + 1]
    article = Article.objects.get(id=i)
    classify = article.aclassify
    l1 = []
    for art in article_all:
        l1.append(str(art.create_time.year) + ' 年 ' + str(art.create_time.month) + ' 月')
    l2 = list(set(l1))
    l2.sort(key=l1.index)
    comment = article.comment_set.all()
    print(comment)
    classifies = Classify.objects.all()
    labels = Label.objects.all()
    context = {'article': article, 'articles1': articles1, 'comment': comment, 'date': l2, 'classify':classify, 'classifies': classifies, 'labels': labels}
    return render(request, 'blog/single.html', context)


def classify(request, i):
    c = Classify.objects.get(id=i)
    article_classall = c.article_set.all()
    article_all = Article.objects.all()
    articles = article_classall[(int(i) - 1) * 4:(int(i) - 1) * 4 + 4]
    # print(articles, articles[0].create_time.year)
    articles1 = article_all[len(article_all) - 3:len(article_all) + 1]
    l1 = []
    for art in article_all:
        l1.append(str(art.create_time.year) + ' 年 ' + str(art.create_time.month) + ' 月')
    l2 = list(set(l1))
    l2.sort(key=l1.index)
    l3 = []
    for i in range(int(len(article_classall) / 4) + 1):
        l3.append(str(i + 1))
    classifies = Classify.objects.all()
    labels = Label.objects.all()
    comments = Comment.objects.all()
    context = {'articles': article_classall, 'articles1': articles1, 'date': l2, 'page': l3,
               'classifies': classifies, 'labels': labels, 'comments': comments}
    return render(request, 'blog/index.html', context)

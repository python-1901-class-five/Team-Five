from django.shortcuts import render, redirect,reverse, HttpResponse,HttpResponseRedirect
from .models import Article, Category, Tags, Comment
from .forms import Commentform
import markdown
# Create your views here.
from django.core.paginator import Paginator


def index(request):
    articles = Article.objects.all()
    paginator = Paginator(articles, 4)
    pagenum = request.GET.get('page')
    print(pagenum)
    pagenum = 1 if pagenum == None else pagenum
    pages = paginator.page(pagenum)
    print(pages.object_list, pages.number)
    context = {'pages': pages}
    return render(request, 'blog/index.html', context)


def single(request, id):
    article = Article.objects.get(id=id)
    article.read_count += 1
    article.save()
    md = markdown.Markdown(extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        'markdown.extensions.toc'
    ])
    article.content = md.convert(article.content)
    article.toc = md.toc
    comments = article.comment_set.all()
    form = Commentform()
    context = {'article': article, 'comments': comments, 'form': form}
    return render(request, 'blog/single.html', context)


def comments(request):
    artid = request.POST['articleid']
    # name = request.POST['name']
    # url = request.POST['url']
    # email = request.POST['email']
    # comment = request.POST['comment']
    post = Article.objects.get(pk=artid)
    # com = Comment()
    # com.name = name
    # com.url = url
    # com.email = email
    # com.text = comment
    # com.post = post
    # com.save()
    form = Commentform(request.POST)
    if form.is_valid():
        form = form.save(commit=False)
        form.post = post
        form.save()
    # return redirect('/blog/single/'+str(artid)+'/')
        return redirect(reverse('blog:single', args=artid))


def choosetime(request, year, month):
    articles = Article.objects.filter(create_time__year=year, create_time__month=month)
    context = {'articles': list(articles)}
    return render(request, 'blog/index.html', context)


def choosecate(request, id):
    articles = Category.objects.get(id=id).article_set.all()
    context = {'articles': articles}
    return render(request, 'blog/index.html', context)


def choosetag(request, id):
    articles = Tags.objects.get(id=id).article_set.all()
    context = {'articles': articles}
    return render(request, 'blog/index.html', context)

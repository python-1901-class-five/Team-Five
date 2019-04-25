from django.contrib.syndication.views import Feed
from django.shortcuts import reverse
from .models import Article


class ArticlePost(Feed):

    title = '文章标题'
    description = '摘要'
    link = '/'

    def items(self):
        return Article.objects.all()

    def item_title(self, item):
        return item.atitle

    def item_description(self, item):
        return item.abstract

    def item_link(self, item):
        return reverse('blog:single', args=(item.id,))

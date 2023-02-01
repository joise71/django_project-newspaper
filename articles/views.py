from django.views.generic import ListView
from . import models


class ArticleListView(ListView):
    model = models.Article
    template_name = 'article_list.html'

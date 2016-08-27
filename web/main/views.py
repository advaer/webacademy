from django.shortcuts import render

# Create your views here.
from .models import Article

from django.views.generic.detail import DetailView
from django.views import View


def index(request):
    posts = Article.objects.all().order_by('-pk')
    return render(request, 'index.html', {'context': posts})


# def article(request, pk):
#     single_article = Article.objects.get(pk=pk)
#     return render(request, 'article.html', {'context': single_article})

# class ArticleView(DetailView):
#     model = Article

class ArticleView(View):
    def get(self, request, pk):
        article = Article.objects.get(pk=pk)
        return render(request, 'main/article_detail.html', {'object': article})

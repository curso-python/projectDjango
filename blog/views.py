from django.shortcuts import render, get_object_or_404
from blog.models import Category, Article
from django.core.paginator import Paginator

# Create your views here.
def list_articles(request):
  articles = Article.objects.all()
  paginator = Paginator(articles, 2)
  page = request.GET.get('page')
  page_articles = paginator.get_page(page)
  return render(request, "articles/list.html", {
    'title': 'Artículos',
    'articles': page_articles
  })

def category(request, category_id):
  category = get_object_or_404(Category, id = category_id)
  articles = Article.objects.filter(categories = category_id)
  return render(request, 'categories/category.html', {
    'category': category,
    'articles': articles
  })

def detail(request, article_id):
  article = get_object_or_404(Article, id=article_id)
  return render(request, 'articles/detail.html', {
    'article': article
  })
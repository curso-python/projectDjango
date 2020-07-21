from django.shortcuts import render
from blog.models import Category, Article

# Create your views here.
def list_articles(request):
  articles = Article.objects.all()
  return render(request, "artilces/list.html", {
    'title': 'Artículos',
    'articles': articles
  })
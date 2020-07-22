from django.urls import path
from . import views

urlpatterns = [

    path('listar/', views.list_articles, name='list'),
    path('categoria/<int:category_id>', views.category, name='category'),
    path('detalle/<int:article_id>', views.detail, name='detail')
]

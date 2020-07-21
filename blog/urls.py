from django.urls import path
from . import views

urlpatterns = [

    path('list/', views.list_articles, name='list'),
    path('category/<int:category_id>', views.category, name='category'),
    path('detail/<int:article_id>', views.detail, name='detail')
]

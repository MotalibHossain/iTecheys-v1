
from django.contrib import admin
from django.urls import path
from django.conf.urls import include

# Views import 
from App_Article.views import Article, ArticleDetails

urlpatterns = [
    path('blog/', Article, name='article'),
    path('article/details/<int:id>', ArticleDetails, name='ArticleDetails'),
]

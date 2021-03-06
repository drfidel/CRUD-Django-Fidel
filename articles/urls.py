from django.urls import path
from .views import AuthorView, SingleAuthorView, ArticleView, SingleArticleView

#app_name = 'articles'

#will help us reverse look up later
urlpatterns = [
    path('authors/', AuthorView.as_view()),
    path('authors/<int:pk>', SingleAuthorView.as_view()),
    path('articles/', ArticleView.as_view()),
    path('articles/<int:pk>', SingleArticleView.as_view()),
]

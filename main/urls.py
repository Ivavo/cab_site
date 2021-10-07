from django.urls import path
from . import views


urlpatterns = [
    path('blog', views.blog_page, name='blog_page'),
    path('blog/add', views.add_blog_article, name='add_article'),
    path('blog/article', views.articlepage, name='article'),
    path('', views.about, name='about'),
    path('record', views.record, name='record_page'),
    path('services', views.services, name='services')
]

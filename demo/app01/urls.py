from django.contrib import admin
from django.urls import path, re_path
#from app01.views import helloworld, article_create, article_detail
from . import views
urlpatterns = [
    path('create/', views.article_create, name = 'article_create'),
    path('<int:article_id>/', views.article_detail, name = 'article_detail'),
    path('list/', views.list, name='article_list')
]
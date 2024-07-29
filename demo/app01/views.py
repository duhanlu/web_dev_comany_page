from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def helloworld(request):
    return HttpResponse('hello world')

def article_create(request):
    return HttpResponse('create an article')

def article_detail(request, article_id):
    return HttpResponse(f'the id of the article is: {article_id}')

def list(request):
    author = 'Freya'
    article_num = 20
    article_list = [
        'The first article: what is Django',
        'The second article: mvt model in django',
        'The third article: views in django'
    ]
    info = {
        'name': 'Freya',
        'age': '0',
        'favorite hobbies': ['running', 'dancing', 'reading']
    }

    return render(request, 'list.html', {
        'author': author,
        'article_num': article_num,
        'article_list': article_list,
        'info': info 
    })
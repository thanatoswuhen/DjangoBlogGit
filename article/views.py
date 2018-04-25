from django.shortcuts import render
from django.http import HttpResponse
from article.models import Article
import datetime

# Create your views here.
# def home(request):
#     return HttpResponse("Hello World, Django")


def home(request):
    post_list = Article.objects.all()  # 获取全部的Article对象
    return render(request, 'home.html', {'post_list': post_list})

def detail(request, id):
    post = Article.objects.all()[int(id)]
    str = ("title = %s, category = %s, date_time = %s, content = %s"
           % (post.title, post.category, post.date_time, post.content))
    return HttpResponse(str)

def test(request):
    return render(request, 'test.html', {'current_time': datetime.time()})

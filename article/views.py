from django.shortcuts import render
from django.http import HttpResponse
from article.models import Article
from datetime import datetime

# Create your views here.
'''def home(request):
    return HttpResponse('hello, world and django!')'''

def home(request):
    post_list = Article.objects.all()
    return render(request, 'home.html', {'post_list': post_list})

'''def test(request):
    return render(request, 'test.html', {'current_time': datetime.now()})'''


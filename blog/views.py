from django.shortcuts import render

from .models import Post, Article

# Create your views here.



def index(request):
	posts = Post.objects.all()
	return render(request, 'blog/index.html', {'posts': posts})


def show(request, id):
	posts = Post.objects.get(pk=id)
	return render(request, 'blog/show.html', {'post': posts} )

def showArticle(request):
	articles = Article.objects.all()
	return render(request,'blog/showArticle.html',{'articles': articles} )

def inscription(request):

	return render(request,'blog/inscription.html', False )
from django.shortcuts import render, get_object_or_404
from .models import Post
from django.utils import timezone
from django.template import RequestContext

def blog(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/blog.html', {'posts': posts})
    
def post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post.html', {'post': post})

def index(request):
    return render(request, 'blog/index.html', {})
def contact(request):
    return render(request, 'blog/contact.html', {})
def cv(request):
    return render(request, 'blog/cv.html', {})    
    
def error_404_view(request, exception):
    return render(request,'blog/errors/404.html')

def error_403_view(request, exception):
    return render(request,'blog/errors/403.html')

def error_400_view(request, exception):
    return render(request,'blog/errors/400.html')

def error_500_view(request):
    return render(request,'blog/errors/500.html')


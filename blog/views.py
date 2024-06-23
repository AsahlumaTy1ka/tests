
from django.shortcuts import render, get_object_or_404
from .models import Post

def home(request):
    posts = Post.objects.all().order_by('-date_posted')
    return render(request, 'home.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post_detail.html', {'post': post})


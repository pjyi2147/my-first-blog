from django.shortcuts import render

# Create your views here.
from .models import Post
from django.utils import timezone
from django.shortcuts import render, get_object_or_404

def post_list(request):
    posts = Post.objects.filter().order_by('-published_date') #필터에 넣으면 안나옴... 왜지...?
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

from django.shortcuts import render
from .models import Post
from django.shortcuts import get_object_or_404

def home(request):
    all_post = Post.objects.all()
    return render(request, 'index.html', {'all_post_list': all_post})


def post_list(request):
    post_list = Post.objects.all()
    return render(request, 'post_list.html', {'post_list':post_list})


def single_post(request, pk):
    #   post = Post.objects.get(pk=pk)
    post = get_object_or_404(Post, pk=pk)
    #print("the post is " , post)
    return render(request, 'single_post.html', {'post': post})
from django.shortcuts import render, get_object_or_404

from .models import Post


def post_list_view(request):
    posts_list = Post.objects.filter(status='pub')
    return render(request, 'blog/posts_list.html', {'posts_list': posts_list})


def post_detail_view(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


def post_create_view(request):
    return render(request, 'blog/post_create.html')
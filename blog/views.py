from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User

from .models import Post
from .forms import NewPostForm


def post_list_view(request):
    posts_list = Post.objects.filter(status='pub').order_by('-datetime_created')
    return render(request, 'blog/posts_list.html', {'posts_list': posts_list})


def post_detail_view(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


def post_create_view(request):
    if request.method == 'POST':  # Post Request
        form = NewPostForm(request.POST)
        if form.is_valid():
            form.save()
            form = NewPostForm()
            return redirect('posts_list')

    else:  # Get Request
        form = NewPostForm()

    return render(request, 'blog/post_create.html', context={'form': form})


def post_edit_view(request, pk):
    post = get_object_or_404(Post, pk=pk)
    form = NewPostForm(request.POST or None, instance=post)

    if form.is_valid():
        form.save()
        return redirect('posts_list')

    return render(request, 'blog/post_create.html', context={'form': form})








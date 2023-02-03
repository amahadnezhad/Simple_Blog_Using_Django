from django.urls import path

from .views import PostListView, PostDetailView, PostCreateView, PostEditView, post_delete_view

urlpatterns = [
    path('', PostListView.as_view(), name='posts_list'),
    path('<int:pk>', PostDetailView.as_view(), name='post_detail'),
    path('create/', PostCreateView.as_view(), name='post_create'),
    path('<int:pk>/edit/', PostEditView.as_view(), name='post_edit'),
    path('<int:pk>/delete/', post_delete_view, name='post_delete'),
]

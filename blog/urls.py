from django.urls import path

from .views import PostListView, post_detail_view, post_create_view, post_edit_view, post_delete_view

urlpatterns = [
    path('', PostListView.as_view(), name='posts_list'),
    path('<int:pk>', post_detail_view, name='post_detail'),
    path('create/', post_create_view, name='post_create'),
    path('<int:pk>/edit/', post_edit_view, name='post_edit'),
    path('<int:pk>/delete/', post_delete_view, name='post_delete'),
]

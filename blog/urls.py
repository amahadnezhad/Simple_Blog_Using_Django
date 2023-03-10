from django.urls import path

from .views import PostListView, post_detail_view, PostCreateView, PostEditView, PostDeleteView

urlpatterns = [
    path('', PostListView.as_view(), name='posts_list'),
    path('<int:pk>', post_detail_view, name='post_detail'),
    path('create/', PostCreateView.as_view(), name='post_create'),
    path('<int:pk>/edit/', PostEditView.as_view(), name='post_edit'),
    path('<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
]

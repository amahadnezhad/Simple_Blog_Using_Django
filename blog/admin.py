from django.contrib import admin

from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'datetime_created', 'status',)
    ordering = ('datetime_created',)

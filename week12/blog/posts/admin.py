from django.contrib import admin
from .models import Post, Comment

class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'published')
    list_display_links = ('id', 'title', 'published')
    search_fields = ('title', 'title', 'body', 'published')
    list_per_page = 25

class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'published', 'message', 'post')
    list_display_links = ('id', 'user', 'published', 'message', 'post')
    search_fields = ('user', 'published', 'message', 'post')
    list_per_page = 25

admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
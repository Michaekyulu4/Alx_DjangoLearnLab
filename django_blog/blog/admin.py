from django.contrib import admin
from .models import Profile
from .models import Post
from .models import Post, Comment

admin.site.register(Profile)
# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "published_date")
    list_filter = ("author", "published_date")
    search_fields = ("title", "content")

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "published_date")
    search_fields = ("title", "content")

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("author", "post", "created_at")
    search_fields = ("author__username", "content")
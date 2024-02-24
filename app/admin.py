from django.contrib import admin
from app.models import Category, Tag, Post, ContentImage, Article

class ContentImageInline(admin.TabularInline):
    model = ContentImage
    extra= 1

class PostAdmin(admin.ModelAdmin):
    inlines = [ContentImageInline]
    list_display = ('title', 'category', 'created_date', 'is_public')
    list_filter = ('category', 'tags', 'is_public')
    search_fields = ('title', 'category__name', 'tags__name', 'content')

admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Article)


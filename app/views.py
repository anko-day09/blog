from typing import Any
from django.db.models import Count, Q
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.http import Http404
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.shortcuts import get_object_or_404
from app.models import Post, Category, Tag, Article

class PostDetailView(DetailView):
    model = Post
    
    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        if not obj.is_public and not self.request.user.is_authenticated:
            raise Http404
        return obj

class IndexView(ListView):
    model = Post
    template_name = 'app/index.html'
    context_object_name = 'posts'
    paginate_by = 6

class CategoryListView(ListView):
    queryset = Category.objects.annotate(
        num_posts=Count('post', filter=Q(post__is_public=True)))

class TagListView(ListView):
    queryset = Tag.objects.annotate(num_posts=Count(
        'post', filter=Q(post__is_public=True)))
    
class CategoryPostView(ListView):
    model = Category  # ここでCategoryモデルを使用
    template_name = 'app/category_post.html'

    def get_queryset(self):
        category_slug = self.kwargs['category_slug']
        self.category = get_object_or_404(Category, slug=category_slug)
        qs = self.category.post_set.filter(is_public=True)  # カテゴリから逆リレーションを仮定しています
        return qs
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.category
        return context

class TagPostView(ListView):
    model = Tag  # Tagモデルを使用
    template_name = 'app/tag_post.html'

    def get_queryset(self):
        tag_slug = self.kwargs['tag_slug']
        self.tag = get_object_or_404(Tag, slug=tag_slug)
        qs = self.tag.post_set.filter(is_public=True)  # タグから逆リレーションを仮定しています
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object'] = self.tag  # またはself.category
        return context

class ArticleDetailView(DetailView):
    model = Article
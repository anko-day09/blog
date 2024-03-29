from django.db import models
from django.utils import timezone
from django.urls import reverse
import markdown

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    description = models.TextField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    tags = models.ManyToManyField(Tag, blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(blank=True, null=True)
    is_public = models.BooleanField(default=False)
    image = models.ImageField(
        upload_to='post_images/', null=True, blank=True)
    
    class Meta:
        ordering = ['-created_date']
    
    def get_absolute_url(self):
        return reverse('app:post_detail', args=[str(self.pk)])
        
    def save(self, *args, **kwargs):
        if self.is_public and not self.published_at:
            self.published_at = timezone.now()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class ContentImage(models.Model):
    post = models.ForeignKey(Post, on_delete=models.PROTECT)
    content_image = models.ImageField(upload_to='post_content_images/')

class Article(models.Model):
    """記事のモデル"""
    title = models.CharField(max_length=255)
    content = models.TextField()

    def markdown_to_html(self):
        """Markdown を HTML に変換して出力
        さらに拡張機能を使用して目次を自動生成する"""
        md = markdown.Markdown(
            extensions=['extra', 'admonition', 'sane_lists', 'toc'])
        html = md.convert(self.content)
        return html
from unicodedata import category, name
from django.db import models

# Create your models here.
class BlogCategory(models.Model):
    name=models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.name


class Blog(models.Model):
    author=models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_author")
    title=models.CharField(max_length=80)
    category=models.ForeignKey(BlogCategory, on_delete=models.CASCADE, related_name="category_blog")
    slug=models.SlugField(max_length=80)
    description=models.CharField(max_length=150)
    # blog_image=models.ImageField(upload_to="Articles/", verbose_name="Image")
    publish_date=models.DateTimeField(auto_now_add=True)
    update_date=models.DateTimeField(auto_now=True)
    # published=models.BooleanField(default=True)
        
    class Meta:
        ordering = ['-publish_date']

    def __str__(self) -> str:
        return self.title

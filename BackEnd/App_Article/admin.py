from django.contrib import admin
from App_Article.models import Blog, BlogCategory

# Register your models here.
admin.site.register(BlogCategory)
admin.site.register(Blog)

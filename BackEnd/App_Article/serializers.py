from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from App_Article.models import Blog, BlogCategory



class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'

    def create(self, validated_data):
        return Blog.objects.create(**validated_data)


class BlogCategorySerializers(serializers.ModelSerializer):
    category_blog=BlogSerializer(many=True, read_only=True)
    class Meta:
        model=BlogCategory
        fields='__all__'

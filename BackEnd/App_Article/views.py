from django.http import HttpResponse
from django.shortcuts import render
# API import
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.response import Response
from rest_framework import status
from App_Article.models import Blog
from App_Article.serializers import BlogSerializer

# Create your views here.

@api_view(['GET', 'POST'])
def Article(request):
    if request.method == 'GET':
        all_post = Blog.objects.all()
        serializer = BlogSerializer(all_post, many=True)
        return Response(serializer.data)
    else:
        return Response(serializer.errors)


def ArticleDetails(request, id):
    pass

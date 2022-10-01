from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework.parsers import JSONParser
# API import
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.response import Response
from rest_framework import status
from App_Article.models import Blog, BlogCategory
from App_Article.serializers import BlogSerializer, BlogCategorySerializers

# Create your views here.

@api_view(['GET', 'POST'])
def BlogCategories(request):
    if request.method == 'GET':
        all_category = BlogCategory.objects.all()
        serializer = BlogCategorySerializers(all_category, many=True)
        return Response(serializer.data)



@api_view(['GET', 'POST'])
def Article(request):
    if request.method == 'GET':
        all_post = Blog.objects.all()
        serializer = BlogSerializer(all_post, many=True)
        return Response(serializer.data)


    if request.method == "POST":
        print("post methode is calling==============================================")
        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
            # return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors)
            # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #Return this if request method is not POST


def ArticleDetails(request, id):
    pass

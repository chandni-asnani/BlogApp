from django.shortcuts import render
from rest_framework import generics
from article.models import Article,Category,Comment
from .pagination import ArticleCustomPagination
from .serializers import ArticleCreateSerializer, CategorySerializer,CommentSerializer
from rest_framework.views import APIView
import django_filters.rest_framework
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend





# Create your views here.


class ArticleList(generics.ListCreateAPIView):
    queryset = Article.objects.all().order_by('-id')
    serializer_class = ArticleCreateSerializer
    filter_backends = [filters.SearchFilter,filters.OrderingFilter,DjangoFilterBackend]
    search_fields = ['title']
    ordering_fields = ['title']
    filterset_fields = ['category']
    pagination_class = ArticleCustomPagination



class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleCreateSerializer
    

class CategoryCreate(generics.CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
class CategoryList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
class CommentCreate(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    
class CommentRetrieveDelete(generics.RetrieveDestroyAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()

    
    

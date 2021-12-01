from django.db.models import fields
from rest_framework import serializers
from .models import Article, Category, Comment
from accounts.serializers import UserSerializer

class CategorySerializer(serializers.ModelSerializer):
     class Meta:
        model = Category
        fields = '__all__'
    
    
class ArticleCreateSerializer(serializers.ModelSerializer):
    # author=serializers.CharField(source='author.first_name')
    # category = CategorySerializer(many=True)
    
    class Meta:
        model = Article
        fields = ['id','author', 'title', 'content', 'image','category']
        
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        # rep["author"] = UserSerializer(instance.author).data['first_name']
        rep["category"] = CategorySerializer(instance.category.all(),many=True).data

        return rep
        
class CommentSerializer(serializers.ModelSerializer):
    # user = serializers.CharField(source='user.first_name')
    # article=serializers.CharField(source='article.title')
    class Meta:
        model = Comment
        fields = ['user','article','comment']
        
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep["user"] = UserSerializer(instance.user).data['first_name']
        rep["article"] = ArticleCreateSerializer(instance.article).data['title']
        return rep
        
    
    

        


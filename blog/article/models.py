from django.db import models
from accounts.models import User

# Create your models here.
class Category(models.Model):
  title = models.CharField(max_length=20, null=True, blank=True)
  image = models.ImageField()
  
  def __str__(self):
    return str(self.title)

  

class Article(models.Model):
  title = models.CharField(max_length=20, null=True, blank=True,unique=True)
  author = models.ForeignKey(User, on_delete=models.CASCADE)
  content = models.TextField()
  image = models.ImageField()
  category = models.ManyToManyField(Category)
  
  def __str__(self):
    return str(self.title)
  
  
class Comment(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  article = models.ForeignKey(Article, on_delete=models.CASCADE)
  comment = models.CharField(max_length=200, null=True, blank=True,unique=True)
  
  def __str__(self):
      return str(self.article)

  

  
  
  
  

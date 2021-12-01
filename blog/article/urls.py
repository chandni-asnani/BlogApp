from django.urls import path
from article import views

    
urlpatterns = [
    path('create/', views.ArticleList.as_view()),
    path('update/<int:pk>/', views.ArticleDetail.as_view()),
    path('categorycreate/', views.CategoryCreate.as_view()),
    path('categorylist/', views.CategoryList.as_view()),
    path('commentcreate/', views.CommentCreate.as_view()),
     path('comment/<int:pk>/', views.CommentRetrieveDelete.as_view()),
    ]

from django.urls import path
from .views import food_post_lists, post_detail, add_post

urlpatterns = [

    path('', food_post_lists, name = 'food posts' ),
    path('post/<int:pk>/', post_detail, name = 'post detail' ),
    path('post/add/', add_post, name = 'add post'),

    
]
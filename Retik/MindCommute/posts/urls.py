from django.urls import path
from .views import PostList, CreatePost, PostDetail

urlpatterns =[
    path('', PostList.as_view(), name = 'forumhome'),
    path('create', CreatePost.as_view(), name = 'createpost'),
    path('posts/<pk>/', PostDetail.as_view(), name = 'postdetail'),
]
